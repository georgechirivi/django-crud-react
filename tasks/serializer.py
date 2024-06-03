from dataclasses import field, fields
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        #fields = ('id', 'titlt', 'description', 'done')
        fields = '__all__'