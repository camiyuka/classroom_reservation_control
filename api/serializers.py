from rest_framework import serializers
from .models import Classroom

class ClassroomSerializer(serializer.Serializers):
    name = serializers.CharField(max_length=100)
    is_available = serializers.BooleanField()
    capacity = serializers.IntegerField()
    number = serializers.IntegerField(max_length=100)
    location = serializers.CharField(max_length=100)
    available_periods = serializers.ListField()