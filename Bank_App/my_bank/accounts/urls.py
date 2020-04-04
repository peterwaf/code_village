from django.contrib import admin
from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = [
    path('accounts/',views.show_accounts,name='accounts'),
    path('accounts/add/',views.AddCustomerAccounts,name="add_account")
]