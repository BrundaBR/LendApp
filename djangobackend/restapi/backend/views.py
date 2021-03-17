from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .models import Signup

from .serializers import SignupSerializer


class SignupView(generics.ListCreateAPIView):
    queryset=Signup.objects.all()
    serializer_class=SignupSerializer
