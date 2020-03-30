from django.contrib import admin
from .models import Student
# Register your models here.

class StudentView(admin.ModelAdmin):
    list_display = ('name','registration_number','school')
    search_fields = ('name','registration_number','school')
    
admin.site.register(Student,StudentView)