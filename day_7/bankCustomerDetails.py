"""
The bank requires a system to manage the customers and their accounts.
The system should allow a bank user to input details of a customer, their account details and balances.
Customer details to be captured are
    1.    First name
    2.    Last name
    3.    Mobile number
    4.    ID number
    5.    Unique Customer  
    6.    Account
The account has the following properties:
    1.    Account Number
    2.    Account Type (current, savings)
    3.    Currency
    4.    Account Balance
Currency has the following properties
    1.    Currency code (KES, USD)
    2.    Currency Name (Kenya shillings)
The requirement is to build a python program that will capture this information for many customers and out put the details

"""
customers = dict()
starter = input('Would you like to add a new customer account? Press 1 for Yes or 2 for No :')

while (starter == '1'):
    customer = dict()
    accountsInfo = dict()
    accountsCurrencyDetails = dict()
    firstName = input('Enter First Name :')
    lastName  = input('Enter Last Name :')
    mobileNumber = int(input('Enter Mobile Number :'))
    idNumber = int(input('Enter Id Number :'))
    uniqueCustomerId = int(input('Customer Unique Id :'))
    customer['First Name'] = firstName
    customer['Last Name'] = lastName
    customer['Mobile No'] = mobileNumber
    customer['Id Number'] = idNumber
    customer['Unique Id'] = uniqueCustomerId
    accountsInfo['Account Number'] = int(input('Enter Account Number : '))
    accountsInfo['Account Type'] = input('Enter Account Type 1 for Savings or 2 Current :')
    if (accountsInfo['Account Type'] == '1'):
        accountsInfo['Account Type'] = 'Savings'
    elif(accountsInfo['Account Type'] == '2'):
        accountsInfo['Account Type'] = 'Current'
    else:
        print('Invalid Input')
        accountsInfo['Account Type'] = input('Enter Account Type eg.Savings or Current :')
        
    accountsCurrencyDetails['Currency Code'] = input('Type 1 for KES or 2 for USD :')
    
    if(accountsCurrencyDetails['Currency Code'] == '1'):
        accountsCurrencyDetails['Currency Code'] = 'KES'
    elif(accountsCurrencyDetails['Currency Code'] == '2'):
        accountsCurrencyDetails['Currency Code'] = 'USD'
    else:
        print('Invalid Input')
        accountsCurrencyDetails['Currency Code'] = input('Enter Currency Type 1 for KES or 2 for USD :')
    
    accountsCurrencyDetails['Currency Name'] = 'Kenya shillings'
    accountsInfo['Account Balance'] = int(input('Enter Account Balance :'))
    accountsInfo['Currency'] = accountsCurrencyDetails
    customer['Account'] = accountsInfo
    #saving all data using customer id
    customers[uniqueCustomerId] = customer
    
    """The account has the following properties:
    1.    Account Number
    2.    Account Type (current, savings)
    3.    Currency
    4.    Account Balance"""
    starter = input('Would you like to add another account? Press 1 for Yes or 2 for No :')

print('Thank you !')

print('===================customers Data=====================')
#obtaining and printng the customers data
for x,y in customers.items():
    print('Customer Id : {}'.format(x))
    print('Name :',y['First Name'],y['Last Name'])
    print('Mobile No :',y['Mobile No'])
    print('Id Number :',y['Id Number'])
    print('Unique Customer Id :',y['Unique Id'])
    #obtaining the account dict items
    currency_holder = y['Account']
    print('Account Number : ',currency_holder['Account Number'])
    print('Account Type :',currency_holder['Account Type'])
    print('Account Balance :',currency_holder['Account Balance'])
    #obtaining the currency dict items
    currencyCodeHolder = currency_holder['Currency']
    print('Currency Code :',currencyCodeHolder['Currency Code'])
    print('Currency Name :',currencyCodeHolder['Currency Name'])
    print('============================')
