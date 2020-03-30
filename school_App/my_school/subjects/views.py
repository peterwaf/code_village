from django.shortcuts import render
from .models import Subject
# Create your views here.

def show_subjects(request):
    all_subjects = Subject.objects.all()
    context = {'all_subjects':all_subjects}
    return render(request,"subjects/subject.html",context)