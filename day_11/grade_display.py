
from myFunctions import  getMean
from myFunctions import  getSum
from myFunctions import  gradingSystem

def displayGrades(studentName,studentRegistration,scoreMath,scoreEnglish,scoreKiswahili):
    print('The student name is {}'.format(studentName))
    print('The student registration number is {} '.format(studentRegistration))
    print('The mean is {} '.format(getMean(getSum(scoreMath,scoreEnglish,scoreKiswahili))))
    print('The grade for English is {}'.format(gradingSystem(scoreEnglish)))
    print('The grade for Kiswahili is {}'.format(gradingSystem(scoreKiswahili)))
    print('The grade for Maths is {}'.format(gradingSystem(scoreMath)))