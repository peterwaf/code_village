"""
Assignment
==========================
1 user enters no of subjects + scores
2 option to end
3 output
-subject
-grade
-mean grade
"""
studentName = input('Enter the student name : ')
studentRegistration = int(input('Enter the Registration Number : '))
numberSubjects = int(input('Enter the Number of subjects : '))
all_scores = dict()
subjectName = ''
subjectScore = 0
if numberSubjects > 0 :
    for i in range(1,numberSubjects+1):
        subjectName = input('Enter the name of the Subject : ')
        subjectScore = int(input('Enter the score for Subject : '))
        all_scores[subjectName] = subjectScore
        

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

printReport(subjectName,subjectScore)
    






    

    
