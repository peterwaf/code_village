from database_connector import dbConnector
from customer import Customer
from validate_customer_data import sender_account_balance
from validate_customer_data import receiver_account_balance
from validate_customer_data import getSenderID
from validate_customer_data import getReceiverID


def sendMoney(user_pin,receipientPhoneNumber,amount):
    connection = dbConnector()
    cursor = connection.cursor()
    sender_balance = sender_account_balance(user_pin)
    receiver_balance = receiver_account_balance(receipientPhoneNumber)
    amount_to_send = amount
    new_sender_balance = sender_balance - amount_to_send
    new_receiver_balance = receiver_balance + amount_to_send
    sender_id = getSenderID(user_pin)
    receiver_id = getReceiverID(receipientPhoneNumber)
    
    #update_sender_balance
    
    sql = "UPDATE accounts SET accountBalance=%s WHERE customer_id=%s;"
    values = (new_sender_balance,sender_id)
    cursor.execute(sql,values)
    connection.commit()
    
    #update receiver balance
    
    sql = "UPDATE accounts SET accountBalance=%s WHERE customer_id=%s;"
    values = (new_receiver_balance,receiver_id)
    cursor.execute(sql,values)
    connection.commit()
    

    