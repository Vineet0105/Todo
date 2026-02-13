from django.shortcuts import render
from .serializer import *
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate

class RegisterAPI(APIView):
    def post(self, request):
        data= request.data
        serializer = RegisterSerializer(data=data)
        if not serializer.is_valid():
            data_json = {
                "Status":True,
                "message":serializer.errors
            }
            return Response(data_json,status.HTTP_400_BAD_REQUEST)

        serializer.save()
        user = User.objects.get(username = data['username'])
        token,_ = Token.objects.get_or_create(user=user)
        data_json = {
            "Status":True,
            "Message": "Account Created",
            "token" : str(token)
            }

        return Response(data_json,status.HTTP_201_CREATED)

class LoginAPI(APIView):

    def get(self,request):
        data= request.data
        serializer = LoginSerializer(data=data)
        if not serializer.is_valid():
            data_json = {
                "Status":True,
                "message":serializer.errors
            }
            return Response(data_json,status.HTTP_400_BAD_REQUEST)

        username = data['username']
        password = data['password']
        user = authenticate(username=username,password=password)
        if user==None:
            data_json = {
                "Status":True,
                "message":serializer.errors
            }             
            return Response(data_json,status.HTTP_400_BAD_REQUEST)
  
        user = User.objects.get(username = data['username'])
        token,_ = Token.objects.get_or_create(user=user)
        data_json = {
            "Status":True,
            "Message": "Account Created",
            "token" : str(token)
            }
        return Response(data_json,status.HTTP_200_OK)

