customers = {879654: {'First Name': 'Peter', 'Last Name': 'Wafula', 'Mobile No': 745789654, 'Id Number': 289456, 'Unique Id': 879654, 'Account': {'Account Number': 1784569874, 'Account Type': 'Current', 'Account Balance': 5000, 'Currency': {'Currency Code': 'KES', 'Currency Name': 'Kenya shillings'}}}, 5547896: {'First Name': 'John', 'Last Name': 'Kissinger', 'Mobile No': 745789654, 'Id Number': 35457896, 'Unique Id': 5547896, 'Account': {'Account Number': 17457964, 'Account Type': 'Savings', 'Account Balance': 87000, 'Currency': {'Currency Code': 'USD', 'Currency Name': 'Kenya shillings'}}}}
for x,y in customers.items():
    print('Customer Id : {}'.format(x))
    print('Name :',y['First Name'],y['Last Name'])
    print('Mobile No :',y['Mobile No'])
    print('Id Number :',y['Id Number'])
    print('Unique Customer Id :',y['Unique Id'])
    currency_holder = y['Account']
    print('Account Number : ',currency_holder['Account Number'])
    print('Account Type :',currency_holder['Account Type'])
    print('Account Balance :',currency_holder['Account Balance'])
    currencyCodeHolder = currency_holder['Currency']
    print('Currency Code :',currencyCodeHolder['Currency Code'])
    print('Currency Name :',currencyCodeHolder['Currency Name'])



    