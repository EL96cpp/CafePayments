from django.db import models
from django.contrib.auth.models import AbstractUser


class Cafe(models.Model):
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house_number = models.SmallIntegerField()


class Employee(models.Model):
    pass