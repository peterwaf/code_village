from database_connector import dbConnector
from add_customer_info import add_customer
from add_customer_info import fetch_CusomerId
from customer import Customer

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
    
    
    
    
    