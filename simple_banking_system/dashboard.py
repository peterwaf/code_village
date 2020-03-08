from customer import Customer
from account import Account
from currency import Currency
#customer attribures : name,idNumber,uniqueID,mobileNo,Pin,account
#currency attributes : code,currencyname
#account attributes accountName,accountNumber,accountType,accountBalance,currency

customers = [] #for storing all customer objects in a list

sender = Customer('Tom Kimani',28147514,54245,254722415876,7854,Account('Jiinue',41257845142847,'Savings',8000,Currency('KES','Kenya Shillings')))
receiver = Customer('Mary Mwende',33147514,1991,2547258415621,8894,Account('Biashara',4120084516000,'Current',10000,Currency('KES','Kenya Shillings')))
#getting accounts info e.g print(sender.account.currency.currencyname)

customers.append(sender) # store sender info in customers list
customers.append(receiver) #store receiver object in customers list
user_input = int(input('Select\n1.Check Balance\n2.Send Money\n0.Exit\n'))

if (user_input == 1):
    user_pin = int(input('Enter Pin :'))
    phone_number = int(input('Enter phone number :'))
    for customer_info in customers:
        if (user_pin == customer_info.Pin and phone_number == customer_info.mobileNo):
            print('Hi {}\nAccount Name :{}\nAccount Number :{}\nAccount Type :{}\nAccount Balance :{}\nCurrency :{}'.format(sender.name,sender.account.accountName,sender.account.accountNumber,sender.account.accountType,sender.account.accountBalance,sender.account.currency.currencyname))
        
        else:
            print('Invalid Pin or Phone Number , Try again')
        break
elif (user_input == 2):
    
    receipientPhoneNumber = int(input('Enter the recepient number :'))
    amount = int(input('Enter Amount to send :'))
    print('You are about to send amount :{} to {} of Phone Number {} , Enter your Pin to send :'.format(amount,receiver.name,receipientPhoneNumber))
    user_pin = int(input('Enter Pin :'))
    
    for customer_info in customers:
        if (user_pin == sender.Pin and receipientPhoneNumber == receiver.mobileNo):
            receiver.account.accountBalance += amount
            sender.account.accountBalance -= amount
            print('Dear {} , {} sent to {} of phone number {} , your balance is {}'.format(sender.name,amount,receiver.name,receiver.mobileNo,sender.account.accountBalance))
            print('Dear {} , you have received {} from {} of {}, your new balance is {}'.format(receiver.name,amount,sender.name,sender.mobileNo,receiver.account.accountBalance))
        else:
            print('Invalid Pin or Phone Number , Try again')
        break

elif(user_input == 0):
    exit()
    


