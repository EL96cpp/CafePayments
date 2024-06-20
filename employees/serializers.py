from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Employee
        fields = ('employee_id', 'password', )