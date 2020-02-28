"""
1.Create a function to input as many students names as possible
2.store in list
"""
studentName = ''
def studentsAdder(studentName):
    students = []
    name = input('Enter name of student :')
    students.append(name)
    question = input('Do you want to add more names ? select : 1 for yes or 2 for no :')
    while question == '1':
        name = input('Enter name of student :')
        students.append(name)
        question = input('Do you want to add more names ? select : 1 for yes or 2 for no :')
    for x in students:
        print(x)
        
studentsAdder(studentName)