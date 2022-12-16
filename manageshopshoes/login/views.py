from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm,ImageStoreForm
from .models import User,Customer,Store
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.backends import ModelBackend
import shutil
import os

path_upload = "/home/truobg/Tài liệu/dulieu/Congty/8-2022/djangotrain/PBL/manageshopshoes/media_upload/photos"
path_root = "/home/truobg/Tài liệu/dulieu/Congty/8-2022/djangotrain/PBL/manageshopshoes/media/photos"

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
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
        try:
            user = authenticate(request, username=username, password=password)
        except Exception as e:
            user = None
        if user is not None:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
        else:
            messages.success(request, 'Login failed')
            return render(request, "login.html")

    return render(request, 'login.html', {'form': form})


def registerPage(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        name = request.POST.get('name')
        confirm_password = request.POST.get("confirmpassword")
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        birthday = request.POST.get('birthday')
        if (password != confirm_password):
            messages.success(request, 'mật khẩu không trùng!')
            return render(request, 'register.html')
        try:
            user = User.objects.get(username=username)
        except:
            user=User(name=name,username=username,phone=phone,email=email)
            user.password =make_password(password)
            customer = Customer(name=name, address=address,
                                email=email, birthday=birthday)
            customer.save()
            # create user
            user = User(name=name, username=username, phone=phone,
                        email=email, customer_id=customer)
            user.password = make_password(password)
            user.save()

            messages.success(request, 'Register success!')
            return redirect('login')

        if user is not None:
            messages.success(request, 'Account already exists!')
    return render(request, 'register.html')

@login_required
def registerStorePage(request):
    current = request.user
    name = request.POST.get('name')
    email = request.POST.get('phone')
    contact = request.POST.get('contact')
    address = request.POST.get('address')
    city = request.POST.get('city')
    fax = request.POST.get('fax')
    form = ImageStoreForm()
    if request.method == 'POST':
        form = ImageStoreForm(request.POST,request.FILES)
        if form.is_valid():
            logo = request.FILES['data']
            user_current = User.objects.get(username=current)
            store = Store(name=name,email=email,contact=contact,city=city,fax=fax,address=address)
            store.save()
            user_current.store_id=store
            user_current.save()
            store.logo = str(store.id)+'brand'+".png"
            store.save()
            print(store.logo)
            upload(logo,str(store.logo))
            handleImageUpload(str(store.logo))
    return render(request, 'registerStore.html', {'current': current,'form' : form})


def upload(f, nameFile):
    if (f.name.split('.')[-1] in ['png', 'jpg', 'webp']):
        file = open(
            os.path.join(path_upload, "stores",nameFile),
            'wb+'
        )
        for chunk in f.chunks():
            file.write(chunk)
        file.close()
    # code handle upload


def handleImageUpload(nameFile):
    shutil.move(path_upload + '/stores' + '/' + nameFile,
                path_root + '/stores' + '/' + nameFile)
