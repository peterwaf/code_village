import mysql.connector
def myDatabaseConnector():
    mydbConnection = mysql.connector.connect(host = "localhost",port="3306",user="root",passwd="pishpan88",database="my_schools_db")
    return mydbConnection

def insertSchoolTodb(school):
    connection = myDatabaseConnector()
    sqlquerry = "insert into schools(code,name,address) values (%s,%s,%s);"
    val = (school.schoolCode,school.schoolname,school.schoolAddress)
    cursor = connection.cursor()
    cursor.execute(sqlquerry,val)
    connection.commit()
    print('Data inserted school in the database')



def insertSubjectTodb(student):
    pass
