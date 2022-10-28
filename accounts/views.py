from urllib import request
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from accounts.models import Message
from .serializers import User_serializer,UserSerializer,Login_serializer,Message_serializer
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
                serializer = UserSerializer(user)
                return Response({'status':'success','token':token.key,'user':serializer.data})
        return Response({'status':'error'})

class LogoutView(APIView):
    permission_classes=[AllowAny]
    def get(self, request):
        if self.request.user:
            logout(request)
            return Response({'status':'your are logged out'},status=HTTP_200_OK)
        return Response(status=HTTP_204_NO_CONTENT)

class MessageView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = Message_serializer
    queryset = Message.objects.all()

    def list(self,request):
        user = self.request.user
        messages = Message.objects.filter(sender=user)
        serializer = Message_serializer(messages)
        return Response({'data':serializer.data},status=HTTP_200_OK)

    def create(self,request):
        serializer = Message_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data},status=HTTP_201_CREATED)
        return Response({'status':'failure'},status=HTTP_206_PARTIAL_CONTENT)