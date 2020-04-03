from django.shortcuts import render
from .models import Customer
from accounts.models import Account
# Create your views here.

def show_all_customers(request):
    all_customers = Customer.objects.all()
    context = {'all_customers':all_customers
               }
    return render(request,"customer/customers.html",context)

def customer_Account_Details(request,cust_id):
    customer_account_info = Account.objects.filter(customer_id=cust_id)
    context = {'customer_account_info':customer_account_info}
    return render(request,"customer/customer_account.html",context)
    