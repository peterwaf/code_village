#import form class from django
from django import forms
#import customer model
from .models import Customer

#create formclass for customer

class CustomerForm(forms.ModelForm):
    #create a meta class
    class Meta:
        model = Customer
        fields = "__all__" #can also use exclude = ['name'] to exclude fields
