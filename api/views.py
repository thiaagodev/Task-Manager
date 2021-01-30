from django.shortcuts import render
from .serializers import *
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.contrib import auth
from django.conf import settings
from .models import *
import jwt

# Create your views here.
class RegisterUserView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class LoginView(GenericAPIView):
    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        user = auth.authenticate(username=username, password=password)
    
        if user:
            auth_token = jwt.encode({'username': user.username}, settings.JWT_SECRET_KEY, algorithm='HS256')

            serializer = UserSerializer(user)

            data = {
                'user': serializer.data,
                'token': auth_token
            }

            return Response(data, status=status.HTTP_200_OK)

            #Send Response
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class TasksListView(ListCreateAPIView):
    serializer_class = TasksSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    
    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)


class TasksDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = TasksSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'
    
    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

