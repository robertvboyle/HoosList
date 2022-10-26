import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin




class User(models.Model):
    username = models.CharField(max_length=20)
    id_num = models.IntegerField()
    image = models.ImageField
    email = models.CharField(max_length=30)


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


