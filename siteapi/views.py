from django.shortcuts import render
from rest_framework import viewsets
from .serializers import LittleGSerializer
from .models import LittleG


class LittleGViewSet(viewsets.ModelViewSet):
    queryset = LittleG.objects.all().order_by('datetime')
    serializer_class = LittleGSerializer