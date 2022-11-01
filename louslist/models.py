import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin




class User(models.Model):
    username = models.CharField(max_length=20)
    id_num = models.IntegerField()
    image = models.ImageField
    email = models.CharField(max_length=30)
    first_name = models.CharField(max_length=20)
    friends = models.ManyToManyField('self', blank=True)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return self.username

class Schedule(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField('Course', blank=True)
    def __str__(self):
        return self.user.username

class Course(models.Model):
    course_id = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    subject = models.CharField(max_length=20)
    number = models.IntegerField()
    section = models.IntegerField()
    credits = models.IntegerField()
    instructor = models.CharField(max_length=20)
    days = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    def __str__(self):
        return self.course_id



# class ClassModel(models.Model):
#     id = models.UUIDField(primary_key=True)
#     instructorName = models.CharField(max_length=100)
#     subject = models.CharField(max_length=8)
#     courseCode = models.IntegerField(max_length=5)
#     component = models.CharField(max_length=5)
#     waitList = models.IntegerField(max_length=3)
#     waitListCap = models.IntegerField(max_length=3)
#     classCap = models.IntegerField(max_length=3)
#     seatsOpen = models.IntegerField(max_length=3)


