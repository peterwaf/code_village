def studentInfo(subjectName,numberOfStudents,numberOfSubjects,studentClass,studentName,studentRegistrationNumber,StudentSubject,StudentScore):
       numberOfStudents = int(input('Enter Number of students :'))
       student_details = dict()
       student_details[studentClass] = [studentName,studentRegistrationNumber,StudentSubject,StudentScore]
       if numberOfStudents > 0:
           for i in range(0,numberOfStudents):
               studentName = input('Student Name :')
               studentRegistrationNumber = input('Student Registration No :')
               studentClass = input('Enter the student class :')
               StudentSubject = int(input('Enter Number of Subjects :'))
               if numberOfSubjects >= 0:
                   
                   
                   
                   