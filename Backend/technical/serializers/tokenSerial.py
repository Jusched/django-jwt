# Django modules
from django.db.models import fields
from rest_framework import serializers

# Local modules
from ..models import Tokens


class TokenSerializer(serializers.ModelSerializer):
    class Meta():
        model = Tokens
        fields = '__all__'
