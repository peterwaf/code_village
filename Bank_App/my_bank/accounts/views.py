from django.shortcuts import render,redirect
from .models import Account
from .forms import AccountForm
from customer.models import Customer
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from transactions.models import Transactions
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.template.loader import render_to_string
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

@login_required(login_url='customer:stafflogin')
def AddCustomerAccounts(request):
    form = AccountForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.info(request,'Account Successfully Added')
    else:
        print('Not Available')
    context = {'form':form}
    
    return render(request,"accounts/add_account.html",context)

@login_required(login_url='customer:customerlogin')
def DepositMoney(request,customer_id):
    customer = Customer.objects.get(pk=customer_id)
    customer_pin = customer.pin
    accounts = Account.objects.filter(customer_id=customer_id)
    if request.method == "POST":
        form = request.POST
        amount = form['amount']
        account = form['accounts']
        pin = form['pin']
        
        try:
            #grab customer account from the DB
            customer_account_object = Account.objects.get(pk=account)
            if (pin != customer_pin):
                messages.info(request,'You have entered a Wrong Pin,Try again.Go to My Money>Deposit Money',extra_tags="pin_error")
                context = {'customer_id':customer_id,'customer':customer,}
                return render(request,"accounts/deposit.html",context)
            
            else:
                customer = Customer.objects.get(pk=customer_id)
                customer_account_number = customer_account_object.accountNumber
                customer_account_balance = customer_account_object.accountBalance
                new_customer_account_amount = customer_account_balance + round(float(amount),2)
                customer_account_currency = customer_account_object.currency_id
                #update customer amount
                customer_account_object.accountBalance = new_customer_account_amount
                #save the amount
                customer_account_object.save()
                #update transactions
                customerCashIn = str(customer_account_currency) + " " +str(round(float(amount),2)) +" Account Deposit"
                trasactionDeposit = Transactions(cashIn=customerCashIn,cashOut='-',transactionFee=0,balance=float(new_customer_account_amount),customer=Customer.objects.get(pk=customer_account_object.pk))
                trasactionDeposit.save()
                #send to customer success template
                context = {'amount':amount,
                        'customer_account_currency':customer_account_currency,
                        'customer_account_number':customer_account_number,
                        'accounts':accounts,
                        'customer_id':customer_id,
                        'customer':customer
                        }
                return render(request,"accounts/depositsuccess.html",context)
            
        except ObjectDoesNotExist as ex:
            messages.info(request,"Account Does Not Exist",extra_tags="account_error")
            customer = Customer.objects.get(pk=customer_id)
            context = {'customer_id':customer_id,'customer':customer,}
            return render(request,"accounts/deposit.html",context)
        
    context = {'accounts':accounts,'customer_id':customer_id,'customer':customer,}
    return render(request,"accounts/deposit.html",context)


def SendSuccessful(request):
    customer = Customer.objects.get(pk=customer_id)
    context = {'customer':customer}
    return render(request,"accounts/send_success.html",context)

@login_required(login_url='customer:customerlogin')
def sendMOney(request,customer_id):
    accounts = Account.objects.filter(customer_id=customer_id)
    if request.method == "POST":
        form = request.POST
        sender_account = form['accounts']
        amount = form['amount']
        receiver_account = form['receiverAccount']
        pin = form['password']
        try:
            customer = Customer.objects.get(pk=customer_id)
            sender_accountinDB = Account.objects.get(id=sender_account)
            sender_balance = sender_accountinDB.accountBalance
            receiver_accountinDB = Account.objects.get(accountNumber=receiver_account) #fetch receiver account info
            if (sender_balance < round(float(amount),2)):
                messages.info(request,'Transaction Failed,You have insufficient funds',extra_tags="InsufficientFunds")
                context = {customer_id:customer_id,'customer':customer,}
                return render(request,"accounts/sendmoney.html",context)
            elif (customer.pin != pin):
                messages.info(request,'You have entered a Wrong Pin,Please Try again',extra_tags="pin_error")
                context = {'customer_id':customer_id,'customer':customer}
                return render(request,"accounts/sendmoney.html",context)
            else:
                customer = Customer.objects.get(pk=customer_id)
                transactionFees = transactionFee(round(float(amount),2))
                sender_name = customer.name
                confirmedReceiverAccount = receiver_accountinDB.accountNumber
                receiverName = receiver_accountinDB.customer_id
                #grab receiver amount
                receiverAMount = receiver_accountinDB.accountBalance
                #update receiver amount
                new_receiverAmount = float(receiverAMount) + round(float(amount),2)
                #update receiver account
                receiver_accountinDB.accountBalance = new_receiverAmount
                #get the sender account object
                senderAccountCurrency = sender_accountinDB.currency_id
                #subtract the sender's balance with new amount
                newSenderBalance =  round(float(sender_balance),2) - round(float(amount),2) - transactionFees
                #update the sender's account balance
                
                sender_accountinDB.accountBalance = newSenderBalance
                sender_accountinDB.save()
                receiver_accountinDB.save()
                
                #add transactions
                senderCashOut = str(senderAccountCurrency) + " " + str(round(float(amount),2))+" sent to " +str(receiverName)+ " of account " + str(receiver_accountinDB.accountNumber)
                receiverCashIn = str(senderAccountCurrency) + " " +str(round(float(amount),2))+" received from "+str(sender_name)+ " of account "+ str(sender_accountinDB.accountNumber)
                trasactionSender = Transactions(cashIn='-',cashOut=senderCashOut,transactionFee=transactionFees,balance=newSenderBalance,customer=Customer.objects.get(pk=customer_id))
                trasactionSender.save()
                trasactionReceiver = Transactions(cashIn=receiverCashIn,cashOut='-',transactionFee=0,balance=float(new_receiverAmount),customer=Customer.objects.get(pk=receiver_accountinDB.pk))
                trasactionReceiver.save()
                context = {'amount':amount,
                        'transactionFees':transactionFees,
                        'newSenderBalance':newSenderBalance,
                        'new_receiverAmount':new_receiverAmount,
                        'confirmedReceiverAccount':confirmedReceiverAccount,
                        'sender_name':sender_name,
                        'receiverName':receiverName,
                        'senderAccountCurrency':senderAccountCurrency,
                        'customer_id':customer_id,
                        'customer':customer,
                        }
                return render(request,"accounts/send_success.html",context)
        
        except ObjectDoesNotExist as ex:
            customer = Customer.objects.get(pk=customer_id)
            messages.info(request,'Account Does Not Exist,Please try again',extra_tags="receiver_Account")
            context = {'customer_id':customer_id,'customer':customer,}
            return render(request,"accounts/sendmoney.html",context)
    
    customer = Customer.objects.get(pk=customer_id)
    context = {
        'accounts':accounts,
        'customer_id':customer_id,
        'customer':customer,
        
        }
    return render(request,"accounts/sendmoney.html",context)

@login_required(login_url='customer:customerlogin')
def CheckBalance(request,customer_id):
    accounts = Account.objects.filter(customer_id=customer_id) #grab all customer accounts and filter
    bal = 0 #global variable
    if request.method == "POST":
        form = request.POST
        account_id = form['account'] #grab the account id
        account_info = Account.objects.get(id=account_id) #grab the pk
        bal = account_info.accountBalance #change global variable
        customer = Customer.objects.get(pk=customer_id)
        context = {'accounts':accounts,'bal':bal,'customer_id':customer_id,'account_info':account_info,'customer':customer}
        return render(request,"accounts/account_info.html",context)
    
    customer = Customer.objects.get(pk=customer_id)
    context = {'accounts':accounts,'customer_id':customer_id,'customer':customer}
    return render(request,"accounts/balance.html",context)


@login_required(login_url='customer:customerlogin')
def WithdrawMoney(request,customer_id):
    accounts  = Account.objects.filter(customer_id=customer_id)
    customer = Customer.objects.get(pk=customer_id)
    if request.method == "POST":
        form = request.POST
        customer_account= form['accounts']
        amount = form['amount']
        transactionFees = transactionFee(round(float(amount),2))
        password = form['password']
        #grab customer account object using the account number filled
        account_obj = Account.objects.get(pk=customer_id)
        accountAmount = account_obj.accountBalance
        if (round(float(amount),2) > accountAmount):
            messages.info(request,"Failed, Insufficient Balance ,Please top up ", extra_tags="insuficient_balance")
            context = {'customer_id':customer_id,'customer':customer,}
            return render(request,"accounts/withdraw.html",context)
        
        elif (customer.pin != password):
            messages.info(request,"Wrong Pin, Please go back and try again", extra_tags="wrong_pin")
            context = {'customer_id':customer_id,'customer':customer}
            return render(request,"accounts/withdraw.html",context)
        
        else:
            customer = Customer.objects.get(pk=customer_id)
            customerAccountName = account_obj.customer_id
            account_currency = account_obj.currency_id
            new_account_balance = round(float(accountAmount),2) - round(float(amount),2)
            account_obj.accountBalance = new_account_balance - transactionFees
            account_obj.save()
            customerCashOut = str(account_currency) + " " + str(round(float(amount),2))+ " withdrawn from your account "
            trasactionWithdraw = Transactions(cashIn='-',cashOut=customerCashOut,transactionFee=transactionFees,balance=new_account_balance,customer=Customer.objects.get(pk=customer_id))
            trasactionWithdraw.save()
            context = {'customer_id':customer_id,
                    'account_currency':account_currency,
                    'transactionFees':transactionFees,
                    'accountAmount':accountAmount,
                    'customerAccountName':customerAccountName,
                    'new_account_balance':new_account_balance,
                    'amount':amount,
                    'customer':customer,
                    
            }
            return render(request,"accounts/withdraw_report.html",context)
        
    context = {'accounts':accounts,'customer_id':customer_id,'customer':customer,
        }
    return render(request,"accounts/withdraw.html",context)

@login_required(login_url='customer:customerlogin')
def ShowTransactions(request,customer_id):
    customertransactions = Transactions.objects.filter(customer=Customer.objects.get(pk=customer_id))
    customer = Customer.objects.get(pk=customer_id)
    context = {'customer_id':customer_id,'customertransactions':customertransactions,'customer':customer,}
    return render(request,'accounts/transactions.html',context)

@login_required(login_url='customer:customerlogin')
def SendMail(request,customer_id):
    customer = Customer.objects.get(pk=customer_id)
    customertransactions = Transactions.objects.filter(customer=Customer.objects.get(pk=customer_id))
    if request.method == "POST":
        form = request.POST
        email = form['email']
        plaintext_context = Context(autoescape=False)  # HTML escaping not appropriate in plaintext
        subject = 'Transaction Statement'
        html_body = render_to_string("accounts/mailer_template.html",{'customertransactions':customertransactions})
        msg = EmailMultiAlternatives(subject=subject, from_email=email,
                                    to=["peterwafulah@gmail.com"], body=html_body)
        msg.attach_alternative(html_body, "text/html")
        msg.send()
        context = {'customer':customer,'email':email}
        return render(request,"accounts/statement_success.html",context)
       
        """
        send_mail('Test Mesage',
                  'Here is the message.',
                  'peterwafulah@gmail.com',
                   [email],
                  fail_silently=False,
                  )
        """
    context = {'customer':customer}
    return render(request,'accounts/mailform.html',context)