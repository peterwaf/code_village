from django.shortcuts import render
from .models import Customer
# Create your views here.

def show_all_customers(request):
    all_customers = Customer.objects.all()
    context = {'all_customers':all_customers
               }
    return render(request,"customer/customers.html",context)