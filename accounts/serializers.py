from dataclasses import fields
from pyexpat import model
from importlib_metadata import files
from rest_framework import serializers
from django.contrib.auth.models import User

class User_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','username','password']

class Login_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']