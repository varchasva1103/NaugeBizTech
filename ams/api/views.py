from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from .models import AttendanceLog, Students, Courses, Departments, Users
from .serializers import AttendanceLogSerializer, CoursesSerializer, DepartmentsSerializer, UsersSerializer, StudentsSerializer

# Create your views here.
class AttendanceLogAPI(viewsets.ModelViewSet):
    queryset = AttendanceLog.objects.all()
    serializer_class = AttendanceLogSerializer 

class CoursesAPI(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer    

class StudentsAPI(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer    

class DepartmentsAPI(viewsets.ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer

class UsersAPI(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = AttendanceLogSerializer    

