from database_connector import dbConnector
from add_customer_info import add_customer
from add_customer_info import fetch_CusomerId
from add_customer_info import add_Account
from add_customer_info import add_Currency
from customer import Customer
from account import Account
from currency import Currency

#get input from the user

num_of_customers = int(input("Enter Number of Customers :"))

for one_customer in range(0,num_of_customers):
    customerName = input("Enter customer name :")
    idNumber = int(input("Enter customer id Number :"))
    uniqIdNumber = int(input("Enter customer Unique id Number :"))
    mobileNumber = input("Enter customer Phone Number starting with 254 :")
    pin = int(input("Enter customer Pin :"))
    
    #initialize the customer object 
    
    customer = Customer(customerName,idNumber,uniqIdNumber,mobileNumber,pin)
    
    #insert customer data into the database
    
    add_customer(customer)
    
    #grab inserted customer id
    
    the_customer_id = fetch_CusomerId(customer)
    
    #add customer account information
    
    accountName = input("Enter Account name :")
    accountNumber = input("Enter account Number :")
    accountType = input("Enter Account Type :")
    accountBalance = int(input("Enter account Balance :"))
    customer_id = the_customer_id
    
    #create instance of account object
    
    account = Account(accountName,accountNumber,accountType,accountBalance,customer_id)
    
    #insert Account info in DB 
    
    add_Account(account)
    
    #add customer currency information
     
    code = input("Enter Currency code :")
    customer_id = the_customer_id
    
    #initialize currency object
    
    currency = Currency(code,Currency.currencyname,customer_id)
    
    #insert currency data into the database
    
    add_Currency(currency)
    
    
    
    
    
    
    
    
    
    
    