from urllib import request
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import User_serializer,Login_serializer
from rest_framework.status import (
    HTTP_200_OK,HTTP_404_NOT_FOUND,HTTP_401_UNAUTHORIZED,HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,HTTP_201_CREATED,HTTP_203_NON_AUTHORITATIVE_INFORMATION,HTTP_206_PARTIAL_CONTENT
) 
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import login,logout,authenticate
# Create your views here.

class Signup(ListCreateAPIView):
    serializer_class = User_serializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()

    def post(self,request):
        serializer = User_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'register successfully'})
        return Response({'status':'failure'})
    
class LoginView(APIView):
    serializer_class = Login_serializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()

    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        print(username,password)
        if username and password:
            user = authenticate(request,username=username,password=password)
            print(user)
            if user:
                login(request,user)
                token, created = Token.objects.get_or_create(user=user)
                serializer = Login_serializer(user)
                return Response({'status':'success','token':token.key,'id':user.id})
        return Response({'status':'error'})

class LogoutView(APIView):
    permission_classes=[AllowAny]
    def get(self, request):
        if self.request.user:
            logout(request)
            return Response({'status':'your are logged out'},status=HTTP_200_OK)
        return Response(status=HTTP_204_NO_CONTENT)