from django.shortcuts import render

# Create your views here.
def show_index(request):
    #no need to call the object
    return render(request,'index/index.html',{})