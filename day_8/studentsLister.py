"""
1.Create a function to input as many students names as possible
2.store in list
"""
studentName = ''
def studentsAdder(studentName):
    students = []
    name = input('Enter name of student :')
    students.append(name)
    question = input('Add more names ? Press : 1 => YES or 2 => NO :')
    while question == '1':
        name = input('Enter name of student :')
        students.append(name)
        question = input('Add more names ? Press : 1 => YES or 2 => NO :')
    print('====Student Names ====')
    for x in students:
        print(x.capitalize())
        
studentsAdder(studentName)