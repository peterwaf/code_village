from database_connector import dbConnector
from customer import Customer
from validate_customer_data import sender_account_balance
from validate_customer_data import receiver_account_balance
from validate_customer_data import getSenderID
from validate_customer_data import getReceiverID
from validate_customer_data import getSenderName
from validate_customer_data import getReceiverName



def sendMoney(user_pin,receipientPhoneNumber,amount):
    connection = dbConnector()
    cursor = connection.cursor()
    sender_balance = sender_account_balance(user_pin)
    if (amount > sender_balance):
        print("You have Insufficient Balance,Please top up :")
        exit()
        
    elif(sender_balance >= amount):
        receiver_balance = receiver_account_balance(receipientPhoneNumber)
        amount_to_send = amount
        new_sender_balance = sender_balance - amount_to_send
        new_receiver_balance = receiver_balance + amount_to_send
        sender_id = getSenderID(user_pin)
        sender_name = getSenderName(user_pin)
        receiver_id = getReceiverID(receipientPhoneNumber)
        receiver_name = getReceiverName(receipientPhoneNumber)
        
        print('Hi {} ,You are about to send {} to {} of phone number {}'.format(amount_to_send,sender_name,amount,receiver_name,receipientPhoneNumber))
        feedback = int(input('1.Confirm\n2.Cancel\n:'))
        if(feedback == 1):
            #update_sender_balance
            sql = "UPDATE accounts SET accountBalance=%s WHERE customer_id=%s;"
            values = (new_sender_balance,sender_id)
            cursor.execute(sql,values)
            connection.commit()
            
            print('{} sent to {}, your new balance is {}'.format(,receiver_name,new_sender_balance))
            
            #update receiver balance
            sql = "UPDATE accounts SET accountBalance=%s WHERE customer_id=%s;"
            values = (new_receiver_balance,receiver_id)
            cursor.execute(sql,values)
            connection.commit()
            
            print('Hi {} , you have received {} from {}.\nYour new balance is {}.Thank you'.format(receiver_name,amount_to_send,sender_name,new_receiver_balance))
            
            
        elif(feedback == 2):
            print('Transaction Canceled.')
            exit()
            
        else:
            print('Invalid Input')
    else:
        print('Invalid Input')
        exit()
    

    