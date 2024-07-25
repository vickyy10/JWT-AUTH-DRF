from django.shortcuts import render
from rest_framework import viewsets
from .models import Person
from .serializer import PersonSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.


class PersonModelViewset(viewsets.ModelViewSet):

    queryset=Person.objects.all()
    serializer_class=PersonSerializer

    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]


    
