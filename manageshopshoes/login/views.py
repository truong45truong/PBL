from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserForm
from .models import Users
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

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
            user = Users.objects.get(login=username,password=password)
        except:
            user=None
        if user is not None:
            user = authenticate(username=username,password=password)
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
            user = Users.objects.get(login=username,password=password)
        except:
            user=Users(name=name,login=username,password=password,phone=phone,email=email)
            user.save()
            messages.success(request,'Register success!')
            return redirect('login')

        if user is not None:
            messages.success(request,'Account already exists!')
    return render(request,'register.html')