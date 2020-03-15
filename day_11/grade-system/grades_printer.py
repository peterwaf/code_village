import math
from mysql_function import myDatabaseConnector
from student_class import Student
from student_subjects import Subject
from student_class import Student
from get_mean import getMean
from grading_system import gradingSystem

def getSubjects():
    myconnection = myDatabaseConnector()
    mycursor = myconnection.cursor()
    students_query = "select * from students;"
    mycursor.execute(students_query)
    studentresults = mycursor.fetchall()
    
    #fetch one by one student
    all_school_subjects = []
    for one_student in studentresults:
        #create instance of student object
        student = Student(one_student[0],one_student[1])
        studid = one_student[2]
        print('Name :{}\nRegNo :{}\nStudent Id :{}'.format(student.name,student.regNumber,studid))
        
        #fetch individual student subjects
        
        #print subjects 
        print('\n======Subjects===== \n')
        
        get_subject_id = "select * from subjects where student_id=%s;"
        new_studId = (studid,)
        mycursor.execute(get_subject_id,new_studId)
        subject_results = mycursor.fetchall()
        
        #get single subject information and assign to subjects object
        
        all_student_subjects = []
        
        for single_subject in subject_results:
            
            #assign Subject object to single_subject
            
            subject = Subject(single_subject[0],single_subject[1],single_subject[2])
        
            #print single subject details
            
            print('{}:{} Grade:{}'.format(subject.subjectName,subject.subjectScore,gradingSystem(subject.subjectScore)))
            all_student_subjects.append(subject.subjectScore)
            
            #add subjects score to all_school_subjects
            
            all_school_subjects.append(subject.subjectScore)
        
        #get mean score and mean grade for all subjects
        
        NoOfSubjects = len(all_student_subjects)
        totalMarks = sum(all_student_subjects)
        meanScore = getMean(totalMarks,NoOfSubjects)
        meanGrade = gradingSystem(meanScore)
        print('Mean Score :{}'.format(meanScore))
        print('Mean Grade :{}'.format(meanGrade))
        print('___________________________\n')
    
    #grab all all_school_subjects_scores
    
    NoOfSchool_Subjects = len(all_school_subjects)
    totalSchoolMarks = sum(all_school_subjects)
    schoolMeanScore = getMean(totalSchoolMarks,NoOfSchool_Subjects)
    schoolMeanGrade = gradingSystem(schoolMeanScore)
    
    print('===Overall School Perfomance===')
    
    print('Mean Score for the school is :{}'.format(schoolMeanScore))
    print('Mean Grade for the school is :{}'.format(schoolMeanGrade))
    
#getSubjects() for testing purposes