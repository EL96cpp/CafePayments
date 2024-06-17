from rest_framework import serializers
from .models import CustomerCard


class CustomerCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerCard
        fields = ('name', 'surname', 'email', 'total_spent')