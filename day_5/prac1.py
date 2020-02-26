class_scores = {'0101': {'Name': 'mathew', 'Class': '1', 'scores': {'english': 45, 'maths': 98}}, '4875': {'Name': 'john', 'Class': '1', 'scores': {'geography': 56}}}

def print_grades():
    for k,v in class_scores.items():
        for m,n in v.items():
            print(v['scores'])
            
print_grades()



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