
from grade_display import displayGrades

studentName = input('Enter the student name : ')
studentRegistration = int(input('Enter the Registration Number : '))
scoreMath = int(input('Enter the score for Math : '))
scoreEnglish = int(input('Enter the score for English : '))
scoreKiswahili = int(input('Enter the score for Kiswahili : '))

displayGrades(studentName,studentRegistration,scoreMath,scoreEnglish,scoreKiswahili)
