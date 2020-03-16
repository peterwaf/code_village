from database_connector import dbConnector
from checkbalance import checkBalance
from customer import Customer

def validatePin_Phone(user_pin,phone_number):
    connection = dbConnector()
    cursor = connection.cursor()
    
    #validate pin
    
    myquery = "select * from customers where pin=%s;"
    pin = (user_pin,)
    cursor.execute(myquery,pin)
    phone_pin_datas = []
    phone_pin_data = cursor.fetchone()
    for num in phone_pin_data:
        phone_pin_datas.append(num)
            
    #validate phone number & pin
    
    if str(phone_number) in phone_pin_datas and user_pin in phone_pin_datas:
        print('Phone Number and Pin Correct')
        checkBalance(user_pin)
    else:
        print('Incorrect Phone Number and or Pin')
        exit()
        
#validatePin_Phone(7878,254785698741)

def ValidateRecipientPhoneNumber(receipientPhoneNumber):
    connection = dbConnector()
    cursor = connection.cursor()
    myquery = "SELECT mobileNumber FROM banking_app.customers;"
    cursor.execute(myquery)
    phones = []
    phones_Numcolumn = cursor.fetchall()
    for phone_num_container in phones_Numcolumn:
        for num in phone_num_container:
            phones.append(num)
    if (receipientPhoneNumber in phones):
        pass
    else:
        print('Phone Not Registered ')
        exit()


def validatePin(user_pin):
    connection = dbConnector()
    cursor = connection.cursor()
    
    #validate pin
    
    myquery = "select * from customers where pin=%s;"
    pin = (user_pin,)
    cursor.execute(myquery,pin)
    phone_pin_datas = []
    phone_pin_data = cursor.fetchone()
    for num in phone_pin_data:
        phone_pin_datas.append(num)
            
    #validate phone number & pin
    
    if user_pin in phone_pin_datas:
        pass
        
    else:
        print('Incorrect Pin')
        exit()


#grab sender_account Bal

def sender_account_balance(user_pin):
    connection = dbConnector()
    cursor = connection.cursor()
    myquery = "select * from customers where pin=%s;"
    pin = (user_pin,)
    cursor.execute(myquery,pin)
    phone_pin_data = cursor.fetchone()
    
    #grab sender name,id and phone
    
    sender_name = phone_pin_data[0]
    sender_id = phone_pin_data[5]
    sender_phone = phone_pin_data[4]
    
    #grab sender account info
    
    myquery = "select * from accounts where customer_id=%s;"
    customer_id = (sender_id,)
    cursor.execute(myquery,customer_id)
    accounts_data = cursor.fetchone()
    
    #accounts balance 
    account_bal = accounts_data[3]
    return account_bal
    
    
#grab receiver _account Bal

def receiver_account_balance(receipientPhoneNumber):
    connection = dbConnector()
    cursor = connection.cursor()
    myquery = "select * from customers where mobileNumber=%s;"
    phonenum = (receipientPhoneNumber,)
    cursor.execute(myquery,phonenum)
    phone_num_data = cursor.fetchone()
    
    #grab sender name,id and phone
    
    receiver_name = phone_num_data[0]
    receiver_id = phone_num_data[5]
    receiver_phone = phone_num_data[4]
    
    #grab sender account info
    
    myquery = "select * from accounts where customer_id=%s;"
    customer_id = (receiver_id,)
    cursor.execute(myquery,customer_id)
    accounts_data = cursor.fetchone()
    
    #accounts balance 
    account_bal = accounts_data[3]
    return account_bal
    

#get sender pin



def getSenderID(user_pin):
    connection = dbConnector()
    cursor = connection.cursor()
    myquery = "select * from customers where pin=%s;"
    pin = (user_pin,)
    cursor.execute(myquery,pin)
    phone_pin_data = cursor.fetchone()
    
    #grab sender name,id and phone
    sender_id = phone_pin_data[5]
    return sender_id


#get receiver Pin

def getReceiverID(receipientPhoneNumber):
    connection = dbConnector()
    cursor = connection.cursor()
    myquery = "select * from customers where mobileNumber=%s;"
    phonenum = (receipientPhoneNumber,)
    cursor.execute(myquery,phonenum)
    phone_num_data = cursor.fetchone()
    #grab sender name,id and phone
    receiver_id = phone_num_data[5]
    return receiver_id

#getReceiverID(254785698741)

#sender_account_balance(7878)
#receiver_account_balance(254785698741)
 
#ValidateRecipientPhoneNumber(2547856987418)
#validatePin(78758)


    
    
    