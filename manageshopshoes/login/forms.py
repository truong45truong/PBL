from django.forms import ModelForm,Form
from login.models import Users
from django import forms


class UserForm(Form):
    username = forms.CharField(label='username')
    password = forms.CharField(widget=forms.PasswordInput())
    
class RegisterForm(ModelForm):
    name = forms.CharField(label='name')
    username = forms.CharField(label='username')
    password1 = forms.CharField(label='password')
    password2 = forms.CharField(label='confirmpassword')
