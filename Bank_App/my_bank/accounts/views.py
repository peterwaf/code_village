from django.shortcuts import render,redirect
from .models import Account
from .forms import AccountForm
from customer.models import Customer
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def show_accounts(request):
    all_customer_accounts = Account.objects.all()
    context = {
        'all_customer_accounts':all_customer_accounts
        }
    return render(request,"accounts/customer_accounts.html",context)


def AddCustomerAccounts(request):
    form = AccountForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('accounts:accounts') #redirect to the list of customer accounts
    context = {'form':form}
    
    return render(request,"accounts/add_account.html",context)

def sendMOney(request):
    context = {
        
        }
    return render(request,"accounts/sendmoney.html",context)

def CheckBalance(request,customer_id):
    accounts = Account.objects.filter(customer_id=customer_id)
    context = {'accounts':accounts
        }
    if request.method == "POST":
        form = request.POST
        account_id = form['account']
        account_info = Account.objects.get(id=account_id)
       
    
    return render(request,"accounts/balance.html",context)

def ShowBalance(request):
    if request.method == "POST":
        form = request.POST
        account_id = form['account']


def WithdrawMoney(request):
    context = {
        }
    return render(request,"accounts/withdraw.html",context)