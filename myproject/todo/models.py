from django.db import models
from datetime import datetime

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class User(models.Model):
    name = models.CharField(max_length=200 , default="")
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200 , default="")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username