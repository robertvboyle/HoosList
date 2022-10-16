import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin




class User(models.Model):
    username = models.CharField(max_length=20)
    id_num = models.IntegerField()
    image = models.ImageField
    email = models.CharField(max_length=30)

