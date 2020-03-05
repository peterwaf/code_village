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
    return allStudentDetails