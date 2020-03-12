import math
from student_class import Student
from student_school import School
from student_subjects import Subject
from grading_system import gradingSystem
from get_mean import getMean
from mysql_function import insertSchoolTodb

allstudents = [] #for storing all student objects in a list

NoOfstudents = int(input('Enter number of students :'))
for x in range(0,NoOfstudents):
    name = input('Enter student name :')
    regNumber = int(input('Enter registration number :'))
    schoolId = input('Enter school id :')
    #insert student into database
    student = Student(name,regNumber,school,subjects)
    insertStudentTodb(student)
    #cursor.execute("insert into students(name,regNo,school_id) values (%s,%s,%s);",(name,regNumber,schoolId))
    #connection.commit()
    
    schoolname = input('Enter school name :')
    schoolAddress = input('Enter school schoolAddress :')
    schoolCode = input('Enter school code :')
    school = School(schoolname,schoolAddress,schoolCode)
    #insert school into database
    insertSchoolTodb(school)
    
    #cursor.execute("insert into schools(code,name,address) values (%s,%s,%s);",(schoolCode,schoolname,schoolAddress))
    #connection.commit()
    
    NoOfsubjects = int(input('Enter number of subjects :'))
    
    subjects = [] #for storing subject objects in a list
    
    for subject in range(0,NoOfsubjects):
        subjectName = input('Enter subject name :')
        subjectScore = int(input('Enter subject score :'))
        subject_id = int(input('Enter subject id;'))
        cursor.execute("insert into subjects(subjectName,subjectScore,subject_id) values (%s,%s,%s);",(subjectName,subjectScore,subject_id))
        connection.commit()
        
        
    one_student = Student(name,regNumber,school,subjects)
    allstudents.append(one_student)
    
print('==== student results ======')

for a in allstudents:
    print('Student Name : ',a.name)
    print('Student Registration No : ',a.regNumber)
    print('School Name :',a.school.schoolname)
    print('School Address :',a.school.schoolAddress)
    subject_scores = []
    for the_subject in a.subjects:
        print('Subject Name :',the_subject.subjectName)
        print('Subject Score :',the_subject.subjectScore)
        subject_scores.append(the_subject.subjectScore)
        print('Grade :',gradingSystem(the_subject.subjectScore))
    sum_of_subjects = sum(subject_scores)
    num_of_subjects = len(subject_scores)
    print('Mean Score {} '.format(getMean(sum_of_subjects,num_of_subjects)))
    print('Mean Grade {}'.format(gradingSystem(getMean(sum_of_subjects,num_of_subjects))))