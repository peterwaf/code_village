from django.contrib import admin
from .models import Subject
# Register your models here.

class SubjectView(admin.ModelAdmin):
    list_display = ('name','score')
    search_fields = ('name','score')
    
admin.site.register(Subject,SubjectView)
