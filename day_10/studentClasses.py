"""grading system
- allow user to input as many students to the system
- sture student objects in a list
- output on each student details
- Student  - name
         - reg number
"""
class Students:
    allStudents = []
    
    def __init__(self,allStudents):
        self.allStudents = allStudents
    
class Student:
    
    def __init__(self,name,regNumber):
        self.name = name
        self.regNumber = regNumber
            

thenumber = []
numberOfStudents = int(input('Enter number of sudents :'))
for x in range(0,numberOfStudents):
    student = Student(name = input('Enter Student Name :'),regNumber = int(input('Enter reg Number :')))
    thenumber.append(student)

allstud = Students(thenumber)
for m in allstud.allStudents:
    print('Name :',m.name.capitalize(),'Registration No :',m.regNumber)

        
        
        
