from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import Inmueble

class InmuebleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inmueble
        fields = '__all__'