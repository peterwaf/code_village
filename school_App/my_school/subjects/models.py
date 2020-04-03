from django.db import models
from students.models import Student
from .grading_system import gradingSystem
# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField()
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'tbl_subjects'
        
    """
    def __str__(self):
        return self.name
    """
    
    def ShowGrade(self):
        return gradingSystem(self.score)
    
    def __str__(self):
        return "{} {}".format(self.name,self.ShowGrade())
    
