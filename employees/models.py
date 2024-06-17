from django.db import models


class Cafe(models.Model):
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house_number = models.SmallIntegerField()


class Employee(models.Model):
    name = models.CharField(max_length=255, null=False)
    surname = models.CharField(max_length=255, null=False)
    cafe = models.ForeignKey('Cafe', on_delete=models.PROTECT)
    password = models.CharField(max_length=255)
