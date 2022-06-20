import email
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import mixins
from rest_framework import generics

from django.contrib.auth import authenticate, login, logout
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

from django.middleware.csrf import get_token
# Create your views here.
        
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserByName(APIView):
    def get(self, request, username):
        user = User.objects.get(username=username)
        serializer = UserSerializer(user)
        return Response(serializer.data)
       
class Login(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                print(request.user)
                return Response({"success": True})
        else:
            return Response({"success": False})
     
class Logout(APIView):
    def post(self, request):
        logout(request)
        return Response({"success": True})
    
def csrf_token(request):
    return JsonResponse({'csrf_token': get_token(request)})

def getUserInfo(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            user = User.objects.get(username=request.user.username)
            user_serializer = UserSerializer(user)
            return JsonResponse(user_serializer.data)