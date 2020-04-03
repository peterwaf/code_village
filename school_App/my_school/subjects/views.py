from django.shortcuts import render,redirect
from .models import Subject
from students.models import Student
from .grading_system import getMean
from .grading_system import gradingSystem
import math
# Create your views here.

def show_subjects(request):
    all_subjects = Subject.objects.all()
    context = {'all_subjects':all_subjects}
    return render(request,"subjects/subject.html",context)

def single_student_subject(request,student_id):
    all_student_subjects = Subject.objects.filter(student=student_id)
    scores = []
    total = 0
    for subj in all_student_subjects:
        total+=subj.score
        scores.append(subj.score)
    num_of_sbj = len(scores)
    mean_score = getMean(sum(scores),num_of_sbj)
    mean_grade = gradingSystem(mean_score)
    student_name = Student.objects.filter(pk=student_id)
    context = {'all_student_subjects':all_student_subjects,'student_name':student_name,'total':total,'mean_score':mean_score,'mean_grade':mean_grade}
    return render(request,"subjects/subject_details.html",context)

def addSubject(request):
    all_students = Student.objects.all()
    if request.method == "POST":
        form = request.POST
        subject = Subject()
        subject.name = form['name']
        subject.score = form['score']
        subject.student = Student.objects.get(pk=form['student']) #get the primary key of the student
        subject.save()
        
        return redirect('subjects:subjects')
    
    context = {'all_students':all_students}
    
    return render(request,'subjects/add_subject.html',context)



    

    