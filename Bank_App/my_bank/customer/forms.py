from .models import Customer
from django.contrib.auth.forms import UserCreationForm
#import form class from django
from django import forms
#import customer model
from user.models import CustomUser
#create formclass for customer

class CustomerForm(forms.ModelForm):
    #create a meta class
    class Meta:
        model = Customer
        fields = "__all__" #can also use exclude = ['name'] to exclude fields

class CreateUserForm(UserCreationForm):
    
    #meta class
    class Meta:
        model = CustomUser
        fields = ['username','email','password1','password2']