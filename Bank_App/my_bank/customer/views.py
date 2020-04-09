from django.shortcuts import render,redirect
from .models import Customer
from accounts.models import Account
from .forms import CustomerForm,CreateUserForm #for importing the default user creation form
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

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

#admin login
"""
def logIn(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index:home')
        else:
            messages.info(request,'Invalid Username or Password')
         
    context = {}
    return render(request,"customer/login.html",context)
"""
#admin register
"""
def Register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account Successfuly Created For {}'.format(user))
    context = {'form':form}
    return render(request,"customer/register.html",context)
"""

#admin logout
"""
def Logout(request):
    logout(request)
    redirect('customer:login')
"""

def customer_Account_Details(request,cust_id):
    customer_account_info = Account.objects.filter(customer_id=cust_id)
    context = {'customer_account_info':customer_account_info}
    return render(request,"customer/customer_account.html",context)


def customerProfile(request):
    context = {
               }
    return render(request,"customer/customer_profile.html",context)


def CustomerLogin(request):
    customer_info = Customer.objects.all()
    if request.method == "POST":
        form = request.POST
        mobileNo = form['mobileNo']
        pin = form['pin']
        mobilenumbers = []
        pins = []
        for log_info in customer_info:
            mobilenumbers.append(log_info.mobileNo)
            pins.append(log_info.pin)
        if (mobileNo in mobilenumbers and pin in pins):
            return redirect('customer:customer_profile')
        else:
            messages.info(request,'Invalid Phone or Pin')
            
    context = {}
    return render(request,"customer/customer_login.html",context)




    