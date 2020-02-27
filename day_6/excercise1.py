numberOfStudents = 0
studentName = ''
studentRegistrationNumber = 0
studentClass = ''
numberOfSubjects = 0
studentSubject = ''
studentScore = 0

def gradingSystem(marks):
    if (marks >=80 and marks <=100):
        return 'A'
    elif(marks >=60 and marks<80):
        return 'B'
    elif(marks>=40 and marks<60):
        return 'C'
    elif(marks<40):
        return 'D'
    else:
        return 'Invalid Grade'
    
def getMean(score,numberSubjects):
    return score/numberSubjects

""""
def printReport(k,v):
    the_sum = 0
    for k,v in all_scores.items():
        the_sum += v
        print('{} Grade : {}'.format(k,gradingSystem(v)))
    print('The mean Grade is {}'.format(getMean(the_sum,numberSubjects)))                  
"""
                             
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

students = studentInfo(numberOfStudents,studentName,studentRegistrationNumber,studentClass,numberOfSubjects,studentSubject,studentScore)                  

print('******** Report Card Start*******')

allStudentScores = 0
allStudentSubjectsCounter = 0

for k,v in students.items():
    print('Name :',v['Name'])
    print('Registration Number :',k)
    print('Class :',v['Class'])
    totalMarks = 0
    allStudentSubjectsCounter += len(v['scores'])
    for subject,score in v['scores'].items():
        totalMarks += score
        allStudentScores += score
        print(subject,score,'Grade :',gradingSystem(score))
    print('Mean Score : ',getMean(totalMarks,len(v['scores'])))
    print('Mean Grade : ',gradingSystem(getMean(totalMarks,len(v['scores']))))
    
#getting the mean score and mean grade for the school

print('The Mean Score for the school is : {}'.format(getMean(allStudentScores,allStudentSubjectsCounter)))
print('The Mean Grade for the school is : {}'.format(gradingSystem(getMean(allStudentScores,allStudentSubjectsCounter))))


"""Get mean score for the school"""
"""Get mean grade for the school"""   
print('******** Report Card End*********')