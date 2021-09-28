from django.db.models import fields
from rest_framework import serializers
from .models import Seminar

class SeminarSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Seminar
        fields = '__all__'
