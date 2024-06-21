from django.db import models


class Cafe(models.Model):
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house_number = models.SmallIntegerField()