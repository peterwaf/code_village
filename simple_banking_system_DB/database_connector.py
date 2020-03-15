import mysql.connector

def dbConnector():
    mydatabase = mysql.connector.connect(host="localhost",
                                         user= "root",
                                         password = "pishpan88",
                                         port = "3306",
                                         database = "banking_app"
    )
    
    return mydatabase


