from django import forms
from .models import Account

class AccountForm(forms.ModelForm):
    #create meta class
    class Meta:
        model = Account
        fields = "__all__"