from django.shortcuts import render,redirect
from .models import School
from students.models import Student
app_name = 'schools'
# Create your views here.

def show_schools(request):
    all_schools = School.objects.all()
    context = {'all_schools':all_schools}
    return render(request,"schools/schools.html",context)

def show_students(request,school_id):
    school_detail=School.objects.filter(pk=school_id) #display school details
    school_student = Student.objects.filter(school=school_id)
    context = {'school_student':school_student,'school_detail':school_detail}
    return render(request,"schools/details.html",context)

def add(request):
    
    if request.method == "POST":
        form = request.POST
        school = School()
        school.name = form['name']
        school.code = form['code']
        school.address = form['address']
        school.no_of_students = form['noOfStudents']
        school.save() #save the details in the database
        
        return redirect('schools:schools') #grab the id of the inserted school
    

    context = {}
    
    return render(request,"schools/add.html",context)

    
