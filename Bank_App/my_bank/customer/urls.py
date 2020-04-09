"""my_bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from . import views
app_name = 'customer'

urlpatterns = [
    path('customers/',views.show_all_customers,name='customers'),
    path('customers/<int:cust_id>/',views.customer_Account_Details,name='customer_details'),
    path('customers/add/',views.addCustomer,name='add_customer'),
    #path('login/',views.logIn,name='login'),
    #path('register/',views.Register,name='register'),
    #path('logout/',views.Logout,name='logout'),
    path('customerlogin/',views.CustomerLogin,name='customerlogin'),
    path('profile/',views.customerProfile,name='customer_profile')
    
]

