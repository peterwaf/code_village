from django.shortcuts import render,redirect
from .models import Customer
from accounts.models import Account
from .forms import CustomerForm
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

def addCustomer(request):
    #save imported form
    form = CustomerForm(request.POST or None,request.FILES or None)

    #if form is valid
    
    if form.is_valid():
        form.save()
        return redirect('customer:customers')
        #save if the form is valid
        #redirect to the list of customers
    context = {'form':form}
    return render(request,"customer/add_customer.html",context)
    

    