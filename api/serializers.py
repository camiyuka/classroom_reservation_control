from rest_framework import serializers

class ClassroomSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    capacity = serializers.IntegerField()
    number = serializers.IntegerField()
    location = serializers.CharField(max_length=100)
    available_periods = serializers.ListField(required=False)