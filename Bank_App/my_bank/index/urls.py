from django.contrib import admin
from django.urls import path
from . import views
app_name = 'index'
urlpatterns = [
    path('',views.show_index,name="home"),
  
]