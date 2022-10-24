from django.forms import ModelForm
from login.models import Users
from django import forms


class UserForm(ModelForm):
    username=forms.CharField(label='username')
    password=forms.CharField(label='password')
    class Meta:
        model = Users
        fields = ['username','password']
class RegisterForm(ModelForm):
    name = forms.CharField(label='name')
    username = forms.CharField(label='username')
    password1 = forms.CharField(label='password')
    password2 = forms.CharField(label='confirmpassword')
