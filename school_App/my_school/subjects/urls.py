from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('subjects/',views.show_subjects,name='subjects'),
    path('subjects/<int:student_id>/',views.single_student_subject,name='subjects'),
]