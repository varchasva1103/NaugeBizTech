from django.db import models

class AttendanceLog(models.Model):
    student = models.ForeignKey('Students', on_delete=models.CASCADE)
    course = models.ForeignKey('Courses', on_delete=models.CASCADE)
    present = models.CharField(max_length=10)
    submitted_by = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now_add=True)

class Courses(models.Model):
    course_name = models.CharField(max_length=50)
    department = models.ForeignKey('Departments', on_delete=models.CASCADE)
    semester = models.IntegerField(max_length=50)
    class_name = models.CharField(max_length=50)
    lecture_hours = models.IntegerField()
    submitted_by = models.CharField(max_length=50)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.course_name

class Users(models.Model):
    USER_TYPES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    )
    type = models.CharField(max_length=50, choices=USER_TYPES)
    full_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    submitted_by = models.CharField(max_length=50)
    updated_at = models.DateField(auto_now=True)

class Departments(models.Model):
    department_name = models.CharField(max_length=50)
    submitted_by = models.CharField(max_length=50)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        self.department_name

class Students(models.Model):
    full_name = models.CharField(max_length=50)
    department = models.ForeignKey('Departments', on_delete=models.CASCADE)
    class_name = models.CharField(max_length=50)
    submitted_by = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name