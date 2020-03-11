import mysql.connector
def myDatabaseConnector():
    mydbConnection = mysql.connector.connect(host = "localhost",port="3306",user="root",passwd="pishpan88",database="my_schools_db")
    return mydbConnection
