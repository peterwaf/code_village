from database_connector import dbConnector

def validatePin_Phone(user_pin,phone_number):
    connection = dbConnector()
    cursor = connection.cursor()
    
    #validate pin
    
    myquery = "SELECT pin FROM banking_app.customers;"
    cursor.execute(myquery)
    all_data = cursor.fetchall()
    all_pins = []
    for tuple_lister in all_data:
        for single_pin in tuple_lister:
            all_pins.append(single_pin)
            
    #validate phone number
    
    myquery2 = "SELECT mobileNumber FROM banking_app.customers;"
    cursor.execute(myquery2)
    all_phones_data = cursor.fetchall()
    all_phones = []
    for phonetuple_lister in all_phones_data:
        for single_phone in phonetuple_lister:
            all_phones.append(single_phone)
    
    if str(phone_number) in all_phones and user_pin in all_pins:
        print('Phone Number and Pin Correct')
    else:
        print('Incorrect Phone Number and or Pin')
        exit()
        
#validatePin_Phone(7878,2547856987418)
    