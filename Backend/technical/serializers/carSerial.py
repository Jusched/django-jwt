# Django modules
from django.db.models import fields
from rest_framework import serializers

# Local modules
from ..models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta():
        model = Car
        fields = '__all__'
