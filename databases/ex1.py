import mysql.connector
mydbConnection = mysql.connector.connect(host = "localhost",port="3306",user="root",passwd="pishpan88",database="my_schools_db")
cursor = mydbConnection.cursor()
cursor.execute("select * from schools")
schools = cursor.fetchall()
for ch in schools:
    print(ch)