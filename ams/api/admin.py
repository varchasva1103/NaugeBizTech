from django.contrib import admin
from .models import Students, Courses, Users, Departments, AttendanceLog 
# Register your models here.
@admin.register(AttendanceLog)
class AttendanceLogAdmin(admin.ModelAdmin):
    list_display = ['id', 'present', 'submitted_by', 'updated_at']

@admin.register(Courses)
class CoursessAdmin(admin.ModelAdmin):
    list_display = ['id', 'course_name', 'class_name','lecture_hours','submitted_by','updated_at']

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name','class_name','submitted_by', 'updated_at']

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'full_name','username','email','password','submitted_by','updated_at']  

@admin.register(Departments)
class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'department_name', 'submitted_by', 'updated_at']      
