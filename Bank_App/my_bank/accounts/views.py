from django.shortcuts import render,redirect
from .models import Account
from .forms import AccountForm
from django.contrib.auth.decorators import login_required
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

def CheckBalance(request):
    context = {
        
        }
    return render(request,"accounts/balance.html",context)

def WithdrawMoney(request):
    context = {
        }
    return render(request,"accounts/withdraw.html",context)