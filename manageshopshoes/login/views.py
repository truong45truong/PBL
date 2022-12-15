from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserForm
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.backends import ModelBackend


# Create your views here.
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user
        except Exception as e:
            return None

@login_required
def logoutUser(request):
    logout(request)
    return redirect('home')
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = UserForm()
    if request.method == 'POST':
        form= UserForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
        try:
            user = authenticate(request,username=username,password=password)
        except Exception as e:
            user=None
        if user is not None:
            login(request,user,backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
        else:
            messages.success(request,'Login failed')
            return render(request, "login.html")

    return render(request,'login.html',{'form':form})
def registerPage(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        name = request.POST.get('name')
        confirm_password = request.POST.get("confirmpassword")
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        if( password != confirm_password):
            messages.success(request,'mật khẩu không trùng!')
            return render(request,'base/register.html')
        try:
            user = User.objects.get(username=username)
        except:
            user=User(name=name,username=username,phone=phone,email=email)
            user.password =make_password(password)
            user.save()
            messages.success(request,'Register success!')
            return redirect('login')

        if user is not None:
            messages.success(request,'Account already exists!')
    return render(request,'register.html')

