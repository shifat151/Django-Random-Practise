from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    pass

class Parent(models.Model):
    name=models.CharField(max_length=10)