from rest_framework import serializers
from .models import Classroom

class ClassroomSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    capacity = serializers.IntegerField()
    number = serializers.IntegerField()
    location = serializers.CharField(max_length=100)
    available_periods = serializers.ListField(required=False)

    def create(self, validated_data):
        return Classroom(**validated_data)