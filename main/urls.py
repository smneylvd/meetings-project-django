from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('signout', views.signout, name='signout'),

    path('add', views.add, name='addTask'),
    path('remove/<int:item_id>', views.deleteItem, name='removeTask'),
    path('filter/<int:day_of_week>', views.filterIndex),

    path('schedule', views.schedule, name='schedule'),
    path('add-to-schedule/<int:weekday>/<str:time>', views.addToSchedule, name='addSchedulePage'),
    path('delete-from-schedule/<int:weekday>/<str:time>', views.deleteFromSchedule),
    path('add-to-schedule', views.addToSchedule, name='addSchedule'),

    path('add-subject', views.addSubject, name='addSubject')
]