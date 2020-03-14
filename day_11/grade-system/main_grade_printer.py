import math
from student_class import Student
from student_school import School
from student_subjects import Subject
from grading_system import gradingSystem
from get_mean import getMean
from mysql_function import insertSchoolTodb
from mysql_function import insertStudentTodb
from mysql_function import getStudentId
from mysql_function import insertSubjectTodb

allstudents = [] #for storing all student objects in a list

NoOfstudents = int(input('Enter number of students :'))
for x in range(0,NoOfstudents):
    name = input('Enter student name :')
    regNumber = int(input('Enter registration number :'))
    student = Student(name,regNumber)
    #insert student into database
    insertStudentTodb(student)

    schoolId = input('Enter school id :')
    schoolname = input('Enter school name :')
    schoolAddress = input('Enter school schoolAddress :')
    schoolCode = input('Enter school code :')
    studentID = getStudentId(student)
    school = School(schoolname,schoolAddress,schoolCode,studentID)
    
    #insert school into database
    insertSchoolTodb(school)
    
    NoOfsubjects = int(input('Enter number of subjects :'))
    
    for one_subject in range(0,NoOfsubjects):
        subjectName = input('Enter subject name :')
        subjectScore = int(input('Enter subject score :'))
        student_id = getStudentId(student)
        subj = Subject(subjectName,subjectScore,student_id)
        insertSubjectTodb(subj)
