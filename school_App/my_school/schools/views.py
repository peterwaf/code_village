from django.shortcuts import render
from .models import School
from students.models import Student

# Create your views here.

def show_schools(request):
    all_schools = School.objects.all()
    context = {'all_schools':all_schools}
    return render(request,"schools/schools.html",context)

def show_students(request,school_id):
    #school_detail=School.objects.get(pk=school_id) if you want to display school details
    school_student = Student.objects.filter(school=school_id)
    context = {'school_student':school_student}
    return render(request,"schools/details.html",context)
    
