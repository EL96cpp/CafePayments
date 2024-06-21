from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone


class EmployeeManager(BaseUserManager):
    def create_user(self, employee_id, first_name, last_name, password):
        if not employee_id:
            raise ValueError("Employee id must be provided!")
        employee = self.model(employee_id=employee_id, first_name=first_name, last_name=last_name)
        employee.set_password(password)
        employee.save(using=self._db)
        return employee

    def create_superuser(self, employee_id, first_name, last_name, password):
        employee = self.create_user(employee_id, first_name, last_name, password)
        employee.is_admin = True 
        employee.is_staff = True
        employee.is_superuser = True
        employee.save(using=self._db)
        return employee


class Employee(AbstractBaseUser, PermissionsMixin):
    employee_id = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = EmployeeManager()

    USERNAME_FIELD = 'employee_id'
    REQUIRED_FIELDS = ['first_name', 'last_name']



