from database_connector import dbConnector

def add_customer(customer):
    connection = dbConnector()
    cursor = connection.cursor()
    
    #insert customers details
    
    sql = "insert into customers(customerName,idNumber,uniqueID,mobileNumber,pin) values (%s,%s,%s,%s,%s);"
    values = (customer.name,customer.idNumber,customer.uniqueID,customer.mobileNo,customer.Pin)
    cursor.execute(sql,values)
    
    connection.commit()
    
    print(cursor.rowcount, "record inserted.")
    

def fetch_CusomerId(customer):
    connection = dbConnector()
    cursor = connection.cursor()
    
    #grab automatically generated customer id
    
    myquery = "select * from customers where idNumber=%s;"
    customer_idNumber = (customer.idNumber,)
    cursor.execute(myquery,customer_idNumber)
    inserted_id = cursor.fetchone()
    customer_id = inserted_id[5]
    return customer_id

def add_Account(account):
    connection = dbConnector()
    cursor = connection.cursor()

    #insert customers account detail
    
    sql = "insert into accounts(accountName,accountNumber,accountType,accountBalance,customer_id) values (%s,%s,%s,%s,%s);"
    values = (account.accountName,account.accountNumber,account.accountType,account.accountBalance,account.customer_id)
    cursor.execute(sql,values)
    connection.commit()
    print(cursor.rowcount, "record inserted.")
    
def add_Currency(currency):
    connection = dbConnector()
    cursor = connection.cursor()
    
    #insert customers account detail

    sql = "insert into currency(currencyName,currencyCode,customer_id) values (%s,%s,%s);"
    values = (currency.code,currency.currencyname,currency.customer_id)
    cursor.execute(sql,values)
    connection.commit()
    print(cursor.rowcount, "record inserted.")
    
    
    
    

