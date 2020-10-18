from django import forms
from django.contrib.auth.models import User

""" class AccountForm(forms.Form):
    username = forms.CharField(label='Your username', max_length=50)
    email = forms.EmailField(label='Your email', max_length=50)
    first_name = forms.CharField(label='Your first_name', max_length=30)
    last_name = forms.CharField(label='Your last_name', max_length=30)
    password = forms.CharField(label='Your password', max_length=30) """

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')