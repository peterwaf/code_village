class Student(): #student class
    def __init__(self,name,regNumber,school,subjects):
        self.name = name
        self.regNumber = regNumber
        self.school = school
        self.subjects = subjects

class School: #school class
    def __init__(self,schoolname,schoolAddress):
        self.schoolname = schoolname
        self.schoolAddress = schoolAddress
         
class Subject:#subject class
    def __init__(self,subjectName,subjectScore):
        self.subjectName = subjectName
        self.subjectScore = subjectScore

allstudents = [] #for storing all student objects in a list
 
NoOfstudents = int(input('Enter number of students :'))
for x in range(0,NoOfstudents):
    name = input('Enter student name :')
    regNumber = int(input('Enter registration number :'))
    schoolname = input('Enter school name :')
    schoolAddress = input('Enter school schoolAddress :')
    school = School(schoolname,schoolAddress)
    NoOfsubjects = int(input('Enter number of subjects :'))
    
    subjects = [] #for storing subject objects in a list
    
    for subject in range(0,NoOfsubjects):
        subjectName = input('Enter subject name :')
        subjectScore = int(input('Enter subject score :'))
        subject = Subject(subjectName,subjectScore)
        subjects.append(subject) # append subject object to subjects
    one_student = Student(name,regNumber,school,subjects)
    allstudents.append(one_student)
    
print('==== student results ======')

for a in allstudents:
    print('Student Name : ',a.name)
    print('Student Registration No : ',a.regNumber)
    print('School Name :',a.school.schoolname)
    print('School Address :',a.school.schoolAddress)
    for the_subject in a.subjects:
        print('Subject Name :',the_subject.subjectName)
        print('Subject Score :',the_subject.subjectScore)

            

    
      


   





