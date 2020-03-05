from student_info import studentInfo
from grading_system import gradingSystem
from get_mean import getMean
from student_info import studentInfo

numberOfStudents = 0
studentName = ''
studentRegistrationNumber = 0
studentClass = ''
numberOfSubjects = 0
studentSubject = ''
studentScore = 0

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
    
#printing the mean score and mean grade for the school

print('The Mean Score for the school is : {}'.format(getMean(allStudentScores,allStudentSubjectsCounter)))
print('The Mean Grade for the school is : {}'.format(gradingSystem(getMean(allStudentScores,allStudentSubjectsCounter))))

print('******** Report Card End*********')

"""Get mean score for the school"""
"""Get mean grade for the school""" 