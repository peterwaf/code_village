import mysql.connector
def myDatabaseConnector():
    mydbConnection = mysql.connector.connect(host = "localhost",port="3306",user="root",passwd="pishpan88",database="my_schools_db")
    return mydbConnection

def insertStudentTodb(student):
    connector = myDatabaseConnector()
    mycursor = connector.cursor()
    
    #insert student data to db
    
    db_querry = "insert into students(name,regNumber) values (%s,%s);"
    values = (student.name,student.regNumber)
    mycursor.execute(db_querry,values)
    connector.commit()
    print(mycursor.rowcount, "record inserted.")
    
    #get inserted student id
    
    tdb_querry =  "select * from students where regNumber=%s;"
    sch_idvalue = (student.regNumber,)
    mycursor.execute(tdb_querry,sch_idvalue)
    
    #fetch inserted student id in the database
    
    inserted_id = mycursor.fetchone()
    print(inserted_id)
    studentID = inserted_id[2]
    return studentID

  
    
def insertSchoolTodb(school):
    connector = myDatabaseConnector()
    mycursor = connector.cursor()
    
    #insert school data to db
    
    db_querry = "insert into schools(schoolName,schoolAddress,schoolCode,student_id) values (%s,%s,%s,%s);"
    values = (school.schoolname,school.schoolAddress,school.schoolCode,school.studentID)
    mycursor.execute(db_querry,values)
    connector.commit()
    print(mycursor.rowcount, "record inserted.")
    
    #get inserted school code
    
    tdb_querry =  "select * from schools where schoolCode=%s;"
    sch_idvalue = (school.schoolCode,)
    mycursor.execute(tdb_querry,sch_idvalue)
    
    #fetch inserted school code in the database
    
    insertedschool = mycursor.fetchone()
    print(insertedschool)

def getStudentId(student):
    connector = myDatabaseConnector()
    mycursor = connector.cursor()
    db_querry = "select * from students where regNumber=%s;"
    sch_idvalue = (student.regNumber,)
    mycursor.execute(db_querry,sch_idvalue)
    studID = mycursor.fetchone()
    return studID[2]


def insertSubjectTodb(subject):
    connector = myDatabaseConnector()
    mycursor = connector.cursor()
    
    # insert student subjects data into the database
    
    db_querry = "insert into subjects(subjectName,subjectScore,student_id) values (%s,%s,%s);"
    values = (subject.subjectName,subject.subjectScore,subject.student_id)
    mycursor.execute(db_querry,values)
    connector.commit()
    
    #get inserted subjects student id
    
    subject_query = "select * from subjects where student_id=%s;"
    stud_id = (subject.student_id,)
    mycursor.execute(subject_query,stud_id)

    #get inserted subjects row
    
    subject_row = mycursor.fetchone()
    print(subject_row)
    
