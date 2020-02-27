customers = dict()
starter = input('Would you like to add a new customer account? Press 1 for Yes or 2 for No :')

while (starter == '1'):
    customer = dict()
    firstName = input('Enter First Name :')
    lastName  = input('Enter Last Name :')
    mobileNumber = int(input('Enter Mobile Number :'))
    idNumber = int(input('Enter Id Number :'))
    uniqueCustomerId = int(input('Customer Unique Id :'))
    customer['First Name '] = firstName
    customer['Last Name '] = lastName
    customer['Mobile No. '] = mobileNumber
    customer['Id Number'] = idNumber
    customer['Unique Id'] = uniqueCustomerId
    accountsInfo = dict()
    accountsInfo['Account Number'] = int(input('Enter Account Number : '))
    accountsInfo['Account Type'] = input('Enter Account Type 1 for Savings or 2 Current ')
    if (accountsInfo['Account Type'] == '1'):
        accountsInfo['Account Type'] = 'Savings'
    elif(accountsInfo['Account Type'] == '2'):
        accountsInfo['Account Type'] = 'Current'
    else:
        print('Invalid ')
        accountsInfo['Account Type'] = input('Enter Account Type eg.Savings or Current ')
    accountsInfo['Currency'] = input('Enter Currency Type 1 for KES or 2 for USD ')
    if (accountsInfo['Currency'] == '1'):
        accountsInfo['Currency'] = 'KES'
    elif(accountsInfo['Currency'] == '2'):
        accountsInfo['Currency'] = 'USD'
    else:
        print('Invalid ')
        accountsInfo['Currency'] = input('Enter Currency Type 1 for KES or 2 for USD ')
    accountsInfo['Currency Name'] = 'Kenya shillings'
    accountsInfo['Account Balance'] = int(input('Enter Account Balance: '))
    customer['Account'] = accountsInfo
    customers[uniqueCustomerId] = customer
    """The account has the following properties:
    1.    Account Number
    2.    Account Type (current, savings)
    3.    Currency
    4.    Account Balance"""
    starter = input('Would you like to add another account? Press 1 for Yes or 2 for No :')

for a,b in customers.items():
    print('Customer Id',a)
    for c,d in b.items():
        print(c,d)
