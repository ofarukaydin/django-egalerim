from django.shortcuts import render
from .models import User, Profile
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_auth.registration.views import RegisterView


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
