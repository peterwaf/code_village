from django.shortcuts import render,redirect
from .models import Account
from .forms import AccountForm
from customer.models import Customer
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from transactions.models import Transactions
# Create your views here.

def transactionFee(amount):
    fee = 0.01 * amount
    return fee


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

def SendSuccessful(request):
    context = {}
    return render(request,"accounts/send_success.html",context)



def sendMOney(request,customer_id):
    accounts = Account.objects.filter(customer_id=customer_id)
    if request.method == "POST":
        form = request.POST
        sender_account = form['accounts']
        amount = form['amount']
        receiver_account = form['receiverAccount']
        customer = Customer.objects.get(pk=customer_id)
        sender_name = customer.name
        receiver_accountinDB = Account.objects.get(accountNumber=receiver_account) #fetch receiver account info
        confirmedReceiverAccount = receiver_accountinDB.accountNumber
        receiverName = receiver_accountinDB.customer_id
        #grab receiver amount
        receiverAMount = receiver_accountinDB.accountBalance
        pin = form['password']
        #update receiver amount
        new_receiverAmount = float(receiverAMount) + float(amount)
        #update receiver account
        receiver_accountinDB.accountBalance = new_receiverAmount
        #get the sender account object
        sender_accountinDB = Account.objects.get(id=sender_account)
        senderAccountCurrency = sender_accountinDB.currency_id
        #subtract the sender's balance with new amount
        newSenderBalance =  sender_accountinDB.accountBalance - float(amount)
        #update the sender's account balance
        sender_accountinDB.accountBalance = newSenderBalance
        sender_accountinDB.save()
        receiver_accountinDB.save()
        
        #add transactions
        
        trasactionSender = Transactions(cashIn=0,cashOut=float(amount),transactionFee=0,balance=newSenderBalance,customer=customer.name)
        trasactionSender.save()
        trasactionReceiver = Transactions(cashIn=float(amount),cashOut=0,transactionFee=0,balance=float(new_receiverAmount),customer=receiver_accountinDB.customer_id)
        trasactionReceiver.save()
        
        context = {'amount':amount,
                   'newSenderBalance':newSenderBalance,
                   'new_receiverAmount':new_receiverAmount,
                   'confirmedReceiverAccount':confirmedReceiverAccount,
                   'sender_name':sender_name,
                   'receiverName':receiverName,
                   'senderAccountCurrency':senderAccountCurrency,
                   'customer_id':customer_id
                   }
        return render(request,"accounts/send_success.html",context)
        
    context = {
        'accounts':accounts,
        'customer_id':customer_id
        }
    return render(request,"accounts/sendmoney.html",context)

def CheckBalance(request,customer_id):
    accounts = Account.objects.filter(customer_id=customer_id) #grab all customer accounts and filter
    bal = 0 #global variable
    if request.method == "POST":
        form = request.POST
        account_id = form['account'] #grab the account id
        account_info = Account.objects.get(pk=account_id) #grab the pk
        bal = account_info.accountBalance #change global variable
        context = {'accounts':accounts,'bal':bal,'customer_id':customer_id,'account_info':account_info}
        return render(request,"accounts/account_info.html",context)
        
    context = {'accounts':accounts,'customer_id':customer_id}
    return render(request,"accounts/balance.html",context)

def ShowBalance(request):
    if request.method == "POST":
        form = request.POST
        account_id = form['account']

def WithdrawMoney(request,customer_id):
    accounts  = Account.objects.filter(customer_id=customer_id)
    if request.method == "POST":
        form = request.POST
        customer_account= form['accounts']
        amount = form['amount']
        password = form['password']
        #grab customer account object using the account number filled
        account_obj = Account.objects.get(id=customer_account)
        accountAmount = account_obj.accountBalance
        customerAccountName = account_obj.customer_id
        account_currency = account_obj.customer_id
        new_account_balance = accountAmount - float(amount)
        account_obj.accountBalance = new_account_balance
        account_obj.save()
        context = {'customer_id':customer_id,
                   'accountAmount':accountAmount,
                   'customerAccountName':customerAccountName,
                   'new_account_balance':new_account_balance,
                   'amount':amount
                
        }
        return render(request,"accounts/withdraw_report.html",context)
        
    context = {'accounts':accounts,'customer_id':customer_id
        }
    return render(request,"accounts/withdraw.html",context)