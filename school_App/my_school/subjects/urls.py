from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('subjects/',views.show_subjects,name='subjects'),
]