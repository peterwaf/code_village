from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('accounts/',views.show_accounts,name='accounts'),
]