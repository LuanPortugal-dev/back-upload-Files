from rest_framework import status
from rest_framework.response import Response

from rest_framework import viewsets

from django.contrib.auth.models import User 

import pandas as pd
import requests

from uploader.serializer import serializers
from uploader import models

class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UsersSerializer
    queryset = models.Users.objects.all()

def createUserInDataBase(username, email, password):
    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        
    user = User.objects.create(
        username=username,
        email=email, 
        password=password
    )

    user.set_password(password)
    user.save()

    return True if user else False

