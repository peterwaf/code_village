students = set()
numOfStudents = int(input('Enter number of students :'))
for x in range(0,numOfStudents):
    studentName = input('Enter Name of student :')
    students.add(studentName)

print("=====Student Names=======")

for student in students:
    print(student.capitalize())