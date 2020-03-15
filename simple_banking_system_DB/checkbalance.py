from database_connector import dbConnector
from customer import Customer

def checkBalance(user_pin):
    connection = dbConnector()
    cursor = connection.cursor()
    
    myquery = "select * from customers where pin=%s;"
    customer_pin = (user_pin,)
    cursor.execute(myquery,customer_pin)
    inserted_pindata = cursor.fetchone()
    
    customer = Customer(inserted_pindata[0],inserted_pindata[1],inserted_pindata[3],inserted_pindata[4],inserted_pindata[5])
    print('Customer Name :{}\nID Number :{}'.format(customer.name,customer.idNumber))
    #fetch customer id
    
    customer_id = inserted_pindata[5]
    
    #fetch account balance from currency
    
    myquery = "select * from banking_app.accounts where customer_id=%s;"
    thecustomer_id = (customer_id,)
    cursor.execute(myquery,thecustomer_id)
    inserted_accountsdata = cursor.fetchone()
    account_balance = inserted_accountsdata[3]
    print('Account balance :',account_balance)
    

#checkBalance(5639)
    