numberOfStudents = 0
studentName = ''
studentRegistrationNumber = 0
studentClass = ''
numberOfSubjects = 0
studentSubject = ''
studentScore = 0

def studentInfo(numberOfStudents,studentName,studentRegistrationNumber,studentClass,numberOfSubjects,studentSubject,studentScore):
    numberOfStudents = int(input('Enter Number of students :'))
    if numberOfStudents > 0:
        allStudentDetails = dict()
        for i in range(0,numberOfStudents):
            studentDetails = dict()
            temporaryStudentData = dict()
            studentName = input('Student Name :')
            studentRegistrationNumber = input('Student Registration No :')
            studentClass = input('Enter the student class :')
            temporaryStudentData['Name'] = studentName
            temporaryStudentData['Class'] = studentClass
            numberOfSubjects = int(input('Enter Number of Subjects :'))
            if numberOfSubjects >= 0:
                studentData = {}
                for subjectCounter in range(0,numberOfSubjects):
                    studentSubject = input('Enter Subject Name : ')
                    studentScore = int(input('Enter Subject Score : '))
                    studentData[studentSubject] = studentScore
                    temporaryStudentData['scores'] = studentData
            allStudentDetails[studentRegistrationNumber] = temporaryStudentData
    print(allStudentDetails)
    
studentInfo(numberOfStudents,studentName,studentRegistrationNumber,studentClass,numberOfSubjects,studentSubject,studentScore)                    
"""
use below functions with above input 

def gradingSystem(marks):
    if (marks >=80 and marks <=100):
        return 'A'
    elif(marks >=60 and marks<80):
        return 'B'
    elif(marks>40 and marks<60):
        return 'C'
    elif(marks<40):
        return 'D'
    else:
        return 'Invalid Grade'

def getMean(score,numberSubjects):
    return score/numberSubjects

def printReport(k,v):
    the_sum = 0
    for k,v in all_scores.items():
        the_sum += v
        print('{} Grade : {}'.format(k,gradingSystem(v)))
    print('The mean Grade is {}'.format(getMean(the_sum,numberSubjects)))                  
                   
   """                