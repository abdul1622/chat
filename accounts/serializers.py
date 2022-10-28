from dataclasses import fields
from pyexpat import model
from statistics import mode
from importlib_metadata import files
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Message

class User_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','username','password']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class Login_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']

class Message_serializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'