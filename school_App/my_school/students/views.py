from django.shortcuts import render,redirect
from .models import Student
from schools.models import School
# Create your views here.

def show_students(request):
    all_students = Student.objects.all()
    context = {'all_students':all_students}
    return render(request,"students/students.html",context)

def addStudent(request):
    all_schools = School.objects.all()
    if request.method == "POST":
        form = request.POST
        student = Student()
        student.name = form['name']
        student.registration_number = form['registration_number']
        student.address = form['address']
        student.age = form['age']
        student.parent_mobile = form['parent_mobile']
        student.school = School.objects.get(pk=form['school'])
        student.save() #save the details in the database
        
        return redirect('students:student_list') #redirect to the link under urls.py
    
    context = {'all_schools':all_schools}
    
    return render(request,"students/add_student.html",context)