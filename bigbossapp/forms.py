from django import forms
from .models import regmodel,addcontestent,votingmodel

class regform(forms.ModelForm):
    class Meta:
        model=regmodel
        fields='__all__'

class loginform(forms.Form):
    username=forms.CharField(label='Enter username',max_length=20,widget=forms.TextInput(attrs={'placeholder':'Enter Username'}))
    password=forms.CharField(label='Enter Password',max_length=20,widget=forms.PasswordInput(attrs={'placeholder':'Enter password'}))

class contestentform(forms.ModelForm):
    class Meta:
        model=addcontestent
        fields='__all__'

class votingform(forms.Form):
   votes=forms.IntegerField()