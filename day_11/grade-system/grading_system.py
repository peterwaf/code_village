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