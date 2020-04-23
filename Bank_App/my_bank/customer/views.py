from django.shortcuts import render,redirect
from .models import Customer
from accounts.models import Account
from .forms import CustomerForm,CreateUserForm #for importing the default user creation form
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
#Check if object does not exist when filtered in the Database
from django.core.exceptions import ObjectDoesNotExist 

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
        messages.info(request,'Customer Successfuly Added')
        #redirect to the list of customers
    context = {'form':form}
    return render(request,"customer/add_customer.html",context)

#admin login

def StafflogIn(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            context = {}
            return render(request,"customer/adminpage.html",context)
        else:
            messages.info(request,'Invalid Username or Password')
    context = {}
    return render(request,"customer/login.html",context)

#user register

def Register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account Successfuly Created For {}'.format(user))
            return redirect('customer:customerlogin')
    context = {'form':form}
    return render(request,"customer/register.html",context)


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


def customerProfile(request,customer_id):
    customer = Customer.objects.get(pk=customer_id)
    context = { 'customer':customer
               }
    return render(request,"customer/customer_profile.html",context)


def CustomerLogin(request):
    if request.method == "POST":
        form = request.POST
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            customer_info = Customer.objects.get(user=user.pk)
            return redirect('customer:customer_profile',customer_info.id)
        else:
            messages.info(request,'Invalid Username or Password')
            
    context = {}
    return render(request,"customer/customer_login.html",context)

def passwordReset(request):
    if request.method == "POST":
        form = request.POST
        number = form['mobileNo']
        access = form['pin']
        
        try:
            #try will pick only if the object does not exist
            customer_info = Customer.objects.get(mobileNo=number)
            new_pin = access
            customer_info.pin = new_pin
            customer_info.save()
            messages.info(request,'Your Pin has been set successfully')
            context = {}
            return render(request,"customer/resetok.html",context)
                
        except ObjectDoesNotExist as ex:
            messages.info(request,'Invalid Phone Number')
            context = {}
            return render(request,"customer/customer_login.html",context)
    context = {}
    return render(request,"customer/passwordreset.html",context)





    