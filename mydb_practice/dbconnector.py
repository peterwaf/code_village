import mysql.connector
mydb = mysql.connector.connect(host="localhost",
                             user= "root",
                             password = "pishpan88",
                             port = "3306",
                             database = "test_db"
)

mycursor = mydb.cursor()
sql = "select * from students;"
mycursor.execute(sql)
data = mycursor.fetchone()
for column in data:
    print(column)
