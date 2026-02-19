from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.serializers import ValidationError



class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)  

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise ValidationError('Username Already Exists')
        return username

    def create(self, validated_data):
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        username = validated_data['username']
        password = validated_data['password']
        user = User.objects.create(first_name=first_name,last_name=last_name,username=username)
        user.set_password(password)
        user.save()

        return validated_data


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)  

    def validate_username(self, username):
        if not User.objects.filter(username=username).exists():
            raise serializers.ValidationError("Username Doesn't Exists")
    
        return username