from django.db import models

class Student(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=10)
# Create your models here.
