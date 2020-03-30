from django.shortcuts import render
from .models import School
# Create your views here.

def show_schools(request):
    all_schools = School.objects.all()
    context = {'all_schools':all_schools}
    return render(request,"schools/schools.html",context)
