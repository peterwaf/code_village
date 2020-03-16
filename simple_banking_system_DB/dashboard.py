from customer import Customer
from account import Account
from currency import Currency
from validate_customer_data import validatePin_Phone
from send_money import sendMoney

#customer attribures : name,idNumber,uniqueID,mobileNo,Pin,account
#currency attributes : code,currencyname
#account attributes accountName,accountNumber,accountType,accountBalance,currency

user_input = int(input('Select\n1.Check Balance\n2.Send Money\n0.Exit\n'))

if (user_input == 1):
    user_pin = int(input('Enter Pin :'))
    phone_number = int(input('Enter phone number :'))
    
    #validate pin & phone and check balance
    
    validatePin_Phone(user_pin,phone_number)
    
 """" 
elif (user_input == 2):
    
    receipientPhoneNumber = int(input('Enter the recepient number :'))
    amount = int(input('Enter Amount to send :'))
    user_pin = int(input('Enter Pin :'))
    sendMoney(receipientPhoneNumber,amount,user_pin)


elif(user_input == 0):
    exit()
"""  


