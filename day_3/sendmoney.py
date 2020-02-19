recipientName = input("Enter name of Recipient :")
recipientPhoneNumber = input("Enter Recipient Phone No :")
amount = int(input("Enter amount :"))

def sendMoney(recipientName,recipientPhoneNumber,amount):
    print('Send {} to {} of {}'.format(amount,recipientName,recipientPhoneNumber))
    confirm = int(input('Press 1 to proceed :'))
    if(confirm==1):
        balance = 5000
        newBalance = balance - amount
        print('confirmed. KES {} sent to {} of {} balance is {}'.format(amount,recipientName,recipientPhoneNumber,newBalance))
sendMoney(recipientName,recipientPhoneNumber,amount)