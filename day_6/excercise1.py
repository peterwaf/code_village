"""Enter no of students
for each student :
    - capture - registration number
    - capture Class
    - capture Name
    - No of subjects
    - Enter subjects & Scores
    -output * Grade for each student
    output * Mean Grade for each student
    
* Meanscore for the class
* Mean grade for the school
"""
numberOfStudents = int(input('Enter the number of students : '))
numberOfSubjects = 0
studentRegistrationNumber = 0
subjectName = ''
studentClass = ''
students = dict()
subjects_scores = dict()


def studentsAdder(numberOfStudents):
    if numberOfStudents > 0:
        for i in range(1,numberOfStudents+1):
            studentName = input('Enter the student name : ')
            studentClass = input('Enter the class : ')
            studentRegistrationNumber = input('Enter the registration number : ')
            
            
            students['class'] = studentClass
            students['name'] = studentName
            students['scores'] = subjects_scores
            
            numberOfSubjects = int(input('Enter No of subjects :'))
            if numberOfSubjects > 0 :
                for j in range(1,numberOfSubjects+1):
                    subjectName = input('Enter the name of the Subject : ')
                    studentScores = int(input('Enter the score for Subject : '))
                    subjects_scores[subjectName] = studentScores             
      
    print(students)
            
studentsAdder(numberOfStudents)

"""Enter no of students
for each student :
    - capture - registration number
    - capture Class
    - capture Name
    - No of subjects
    - ENter subjects & Scores
    -output * Grade for each student
    output * Mean Grade
    
* Meanscore for the class
* Mean grade for the school

"""
