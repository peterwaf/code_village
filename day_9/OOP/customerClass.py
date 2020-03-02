class Customer:
    def __init__(self,customerName,accountNumber,currency):
        self.customerName = customerName
        self.accountNumber = accountNumber
        self.currency = currency
            
    def showCustomerDetails(self):
        print('===== Customer Details =====')
        print("Account Name : {}\nAccount Number :{}\nCurrency : {}".format(self.customerName,self.accountNumber,self.currency))

peter = Customer(customerName = input('Enter Customer Name :'),accountNumber = int(input('Enter Account Number : ')),currency='KES')
peter.showCustomerDetails()


    
        