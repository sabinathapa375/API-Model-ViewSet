from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class StudentViewset(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class =  StudentSerializer
    