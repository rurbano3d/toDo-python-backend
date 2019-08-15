from django.shortcuts import render
from rest_framework import viewsets
from .models import Lista
from .serializers import ListaSerializer

class ListaViewSet (viewsets.ModelViewSet):
    queryset = Lista.objects.all()
    serializer_class = ListaSerializer

