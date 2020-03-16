from database_connector import dbConnector
from checkbalance import checkBalance

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

def recipientPhoneNumber(receipientPhoneNumber):
    connection = dbConnector()
    cursor = connection.cursor()
    myquery = "select * from customers where mobileNumber=%s;"
    phoneval = (receipientPhoneNumber,)
    cursor.execute(myquery,phoneval)
    phone_Numcolumn = cursor.fetchone()
    #print(phone_Numcolumn)
    
    