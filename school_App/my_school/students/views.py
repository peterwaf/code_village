from django.shortcuts import render
from .models import Student
# Create your views here.

def show_students(request):
    all_students = Student.objects.all()
    context = {'all_students':all_students}
    return render(request,"students/students.html",context)
