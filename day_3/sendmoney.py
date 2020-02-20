balance = 5000
recipientName = input("Enter name of Recipient :")
recipientPhoneNumber = input("Enter Recipient Phone No :")
amount = int(input("Enter the amount :"))
if (len(str(recipientPhoneNumber))!=10):
        print('Failed,Invalid Phone number,Please use 10 digit format 07XXXXXXXX')
elif (amount>balance):
        print('You have insufficient funds,Please top up your amount')
else:
        def sendMoney(recipientName,recipientPhoneNumber,amount):
                print('Send {} to {} of {}'.format(amount,recipientName,recipientPhoneNumber))
                confirm = int(input('Press 1 to proceed :'))
                if(confirm==1):
                        transactionAmount = amount * 0.01
                        newBalance = balance - amount - transactionAmount
                        print('confirmed. KES {} sent to {} of {} balance is {}, transaction fee is {}'.format(amount,recipientName,recipientPhoneNumber,newBalance,transactionAmount))
        sendMoney(recipientName,recipientPhoneNumber,amount)