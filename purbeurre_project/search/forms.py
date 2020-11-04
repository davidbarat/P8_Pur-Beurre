from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Your email', max_length=50)
    password = forms.CharField(label='Your password', max_length=30)
    username = forms.CharField(label='Your username', max_length=30)
    first_name = forms.CharField(label='Your first_name', max_length=30)
    last_name = forms.CharField(label='Your last_name', max_length=30)
    class Meta():
        model = User
        fields = ('email','password', 'first_name', 'last_name', 'username')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        # fields = ('email','password')
        fields = ('username','password')
