from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Hello
from .serializer import HelloSerializer
# Create your views here.
class HelloViewSet(ListCreateAPIView):
    queryset = Hello.objects.all()
    serializer_class = HelloSerializer

class HelloDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Hello.objects.all()
    serializer_class= HelloSerializer