from django.contrib.auth.models import User as AdminUser
from django.db import models


# Create your models here.

class User(AdminUser):
    group = models.CharField('group', max_length=255)


class List(models.Model):
    title = models.CharField('name', max_length=1024)
    description = models.CharField('name', max_length=1024, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deadline = models.DateTimeField(null=True)
    color = models.CharField('color', default="orange", max_length=50)

    def __str__(self):
        return self.title


class Subject(models.Model):
    name = models.CharField('name', max_length=144)
    color = models.CharField('color', default="orange", max_length=50)


class Schedule(models.Model):
    day = models.IntegerField()
    time = models.CharField('time', max_length=20)
    type = models.CharField('type', max_length=20)
    cab = models.CharField('cab', max_length=64, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
