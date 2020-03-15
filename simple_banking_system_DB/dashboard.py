from customer import Customer
from account import Account
from currency import Currency
from validate_customer_data import validatePin_Phone

#customer attribures : name,idNumber,uniqueID,mobileNo,Pin,account
#currency attributes : code,currencyname
#account attributes accountName,accountNumber,accountType,accountBalance,currency

user_input = int(input('Select\n1.Check Balance\n2.Send Money\n0.Exit\n'))

if (user_input == 1):
    user_pin = int(input('Enter Pin :'))
    phone_number = int(input('Enter phone number :'))
    validatePin_Phone(user_pin,phone_number)
    
"""   
elif (user_input == 2):
    
    receipientPhoneNumber = int(input('Enter the recepient number :'))
    amount = int(input('Enter Amount to send :'))
    if amount > sender.account.accountBalance:
        print('You have insufficient funds.Please top up.')
    else:
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
"""  


