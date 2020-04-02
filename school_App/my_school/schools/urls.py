from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('schools/',views.show_schools,name='schools'),
    path('schools/<int:school_id>/',views.show_students,name='students'),
    #path('schools/add/',views.add,name='add'),
]