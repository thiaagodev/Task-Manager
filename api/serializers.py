from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=5)
    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email = email).exists():
            raise serializers.ValidationError({'email', ('Email is already in use.')})
        return super().validate(attrs)

    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class TasksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'created_at', 'task_finish']

