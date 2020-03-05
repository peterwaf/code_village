studentName = input('Enter the student name : ')
studentRegistration = int(input('Enter the Registration Number : '))

scoreMath = int(input('Enter the score for Math : '))
scoreEnglish = int(input('Enter the score for English : '))
scoreKiswahili = int(input('Enter the score for Kiswahili : '))

def gradingSystem(marks):
    if (marks >=80 and marks <=100):
        return 'A'
    elif(marks >=60 and marks<80):
        return 'B'
    elif(marks>40 and marks<60):
        return 'C'
    elif(marks<40):
        return 'D'

def getSum(a,b,c):
    return a + b + c

def getMean(score):
    return score/3

def displayGrades():
    print('The student name is {}'.format(studentName))
    print('The student registration number is '.format(studentRegistration))
    print('The mean is {} '.format(getMean(getSum(scoreMath,scoreEnglish,scoreKiswahili))))
    print('The grade for English is {}'.format(gradingSystem(scoreEnglish)))
    print('The grade for Kiswahili is {}'.format(gradingSystem(scoreKiswahili)))
    print('The grade for Maths is {}'.format(gradingSystem(scoreMath)))
    
displayGrades()




    

    
