from django import forms

class AccountForm(forms.Form):
    username = forms.CharField(label='Your username', max_length=50)
    email = forms.EmailField(label='Your email', max_length=50)
    first_name = forms.CharField(label='Your first_name', max_length=30)
    last_name = forms.CharField(label='Your last_name', max_length=30)
    password = forms.CharField(label='Your password', max_length=30)