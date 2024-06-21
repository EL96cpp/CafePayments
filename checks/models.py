from django.db import models
from employees.models import Employee
from cafes.models import Cafe
from customers.models import CustomerCard


class Check(models.Model):
    employee = models.ForeignKey(to=Employee, on_delete=models.PROTECT)
    cafe = models.ForeignKey(to=Cafe, on_delete=models.PROTECT)
    customer = models.ForeignKey(to=CustomerCard, on_delete=models.PROTECT, null=True)
    discount = models.SmallIntegerField()
    total_no_discount = models.IntegerField()
    total_with_discount = models.IntegerField()
    order = models.JSONField()
    date = models.DateTimeField()
