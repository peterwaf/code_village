from django.contrib import admin
from django.urls import path
from . import views

app_name='students'

urlpatterns = [
    path('students/',views.show_students,name='student_list'),
    path('students/add/',views.addStudent,name='add'),
]