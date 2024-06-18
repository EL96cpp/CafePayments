from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class CustomerCard(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, null=False)
    total_spent = models.IntegerField(default=0)
    discount = models.SmallIntegerField(default=0)