from mysql_function import myDatabaseConnector
from student_class import Student
from student_subjects import Subject
from student_class import Student

def getSubjects():
    myconnection = myDatabaseConnector()
    mycursor = myconnection.cursor()
    students_query = "select * from students;"
    mycursor.execute(students_query)
    studentresults = mycursor.fetchall()
    
    for studentid in studentresults:
        for num in studentid:
            get_subject_id = "select * from subjects where student_id=%s;"
            studid = (num,)
            mycursor.execute(get_subject_id,studid)
            subject_results = mycursor.fetchall()
            # get single subject:
            for subj in subject_results:
                
                #assign subjects results tuple to subjects object
                
                subjects = Subject(subj[0],subj[1],subj[2])
                print('Subject :{}\nScore:{} '.format(subjects.subjectName,subjects.subjectScore))
    
getSubjects()