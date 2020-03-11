from mysql_function import myDatabaseConnector
cursor = myDatabaseConnector.cursor()
cursor.execute("insert into schools(code,name,address) values ('7878','mombasa high','0042-5421');")
mydbConnection.commit()
