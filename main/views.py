import datetime
from pprint import pprint

from django.contrib.auth import authenticate, login as LogIn
from django.contrib.auth import logout as LogOut
from django.http import response
from django.shortcuts import render
from django.shortcuts import redirect
from .models import List, User, Subject, Schedule


def signout(request):
    LogOut(request)
    return redirect(login)


def login(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(username=request.POST['email'], password=request.POST['password'])
            LogIn(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect(index)
        except:
            return render(request, 'main/login.html', {
                'invalid': 'Incorrect username or password'
            })
    return render(request, 'main/login.html')


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        group = request.POST.get('group')
        password = request.POST.get('password')
        user2 = User(username=email, email=email, first_name=name, password=password, group=group)
        user2.save()
        return redirect('/')
    return render(request, 'main/register.html')


def deleteItem(request, item_id):
    List.objects.get(id=item_id).delete()
    return redirect('/')


def add(request):
    if request.method == 'POST':
        id = request.user.id
        title = request.POST['title']
        description = request.POST['description']
        color = request.POST['color']
        deadline = request.POST['deadline']
        new_item = List(title=title, user_id=id, description=description, color=color, deadline=deadline)
        new_item.save()
        return redirect('/')


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'main/welcome.html')
    id = request.user.id
    items = List.objects.filter(user_id=id)
    return render(request, 'main/index.html', {'items': items})


def filterIndex(request, day_of_week):
    print(day_of_week)
    if not request.user.is_authenticated:
        return render(request, 'main/welcome.html')

    id = request.user.id
    # if day_of_week == 'monday' :
    days = [
        'monday',
        'tuesday',
        'wednesday',
        'thursday',
        'friday',
        'saturday',
        'sunday'
    ]

    items = List.objects.filter(user_id=id). \
        filter(deadline__week_day=day_of_week). \
        exclude(deadline__gt=next_weekday(datetime.date.today(), 0))

    return render(request, 'main/index.html', {'items': items, 'day': days[day_of_week - 1]})


def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:  # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)


def schedule(request):
    weekdays = [1, 2, 3, 4, 5, 6, 7]
    timeline = [
        '08:30-09:20',
        '09:30-10:20',
        '10:40-11:30',
        '11:40-12:30',
        '14:00-14:50',
        '15:00-15:50',
        '16:10-17:00',
        '17:10-18:00',
        '18:10-19:00',
        '19:10-20:00',
        '20:10-21:00',
    ]
    data = {}
    for time in timeline:
        data[time] = {}
        for day in weekdays:
            lesson = Schedule.objects.filter(time=time, day=day, user_id=request.user.id)

            data[time][day] = '+'

            if lesson:
                data[time][day] = lesson[0]
                print('SUBJECT:', data[time][day])
    return render(request, 'main/schedule.html', {
        'timeline': timeline,
        'weekdays': weekdays,
        'data': data
    })


def addToSchedule(request, weekday=None, time=None):
    if request.method == 'POST':
        type = request.POST['type']
        cab = None
        if request.POST['cab']:
            cab = request.POST['cab']
        subject = request.POST['subject']
        user = request.user.id
        values = request.POST.getlist('values[]')
        for val in values:
            day, time = val.split('/')

            if len(Schedule.objects.filter(user_id=user).filter(time=time).filter(day=day)):
                return redirect('schedule')

            newSc = Schedule(day=day, time=time, type=type, cab=cab, subject_id=subject, user_id=user)
            newSc.save()

        return redirect('schedule')

    weekdays = [1, 2, 3, 4, 5, 6, 7]
    timeline = [
        '08:30-09:20',
        '09:30-10:20',
        '10:40-11:30',
        '11:40-12:30',
        '14:00-14:50',
        '15:00-15:50',
        '16:10-17:00',
        '17:10-18:00',
        '18:10-19:00',
        '19:10-20:00',
        '20:10-21:00',
    ]
    data = {}
    for period in timeline:
        data[period] = {}
        for day in weekdays:
            lesson = Schedule.objects.filter(time=period, day=day, user_id=request.user.id)

            data[period][day] = '+'

            if lesson:
                data[period][day] = lesson[0]
                print('SUBJECT:', data[period][day])
    subjects = Subject.objects.all()
    return render(request, 'main/add-to-schedule.html', {
        'subjects': subjects,
        'weekday': weekday,
        'timeline': timeline,
        'weekdays': weekdays,
        'data': data,
        'time': time,
    })

def deleteFromSchedule(request, weekday=None, time=None):
    lesson = Schedule.objects.filter(time=time, day=weekday, user_id=request.user.id)
    lesson.delete()
    return redirect('schedule')

def addSubject(request):
    if request.method == 'POST':
        name = request.POST['name']
        if Subject.objects.filter(name=name):
            return redirect('schedule')
        color = request.POST['color']
        newSubj = Subject(name=name, color=color)
        newSubj.save()
        return redirect('schedule')

    return render(request, 'main/add-subject.html')
