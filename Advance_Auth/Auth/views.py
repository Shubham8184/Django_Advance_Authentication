from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail




def Homeview(request):
    template_name='Auth/Home.html'
    return render(request,template_name)

def Registerview(request):
    form=RegisterForm()
    if request.method == 'POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            email=request.POST.get('email')
            user=request.POST.get('username')
            uemail=User.objects.filter(email=email).first()
            if uemail is None:
                form.save()
                subject='Registration'
                admin='bobadesp1234@gmail.com'
                msj=f'Hello {user} ,Welcome..!!! Thank you for joining with us,Please save your password for future and click on link for log in and enjoy the services Link:-http://127.0.0.1:8000/auth/login/ '
                send_mail(subject,msj,admin,[email],fail_silently=True)
                messages.error(request,'Thank you for registration')
                return redirect('login')
            messages.error(request,'Email Address is already register')
        messages.error(request,'Please provide valid information')
    template_name='Auth/Register.html'
    context={'form':form}
    return render(request,template_name,context)

def Loginview(request):
    if request.method == 'POST':
        u=request.POST.get('uname')
        p=request.POST.get('password')
        user=authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            return redirect('home')
        messages.error(request,'Invalid Credential')
    template_name='Auth/Login.html'
    return render(request,template_name)

def Logoutview(request):
    logout(request)
    return redirect('login')

def Changepassview(request):
    if request.method == 'POST':
        u=request.POST.get('uname')
        p=request.POST.get('password')
        np=request.POST.get('newpass')
        cp=request.POST.get('cpass')
        email=request.POST.get('email')
        user=authenticate(username=u,password=p)
        if user and np==cp:
            usr=User.objects.get(username=u)
            npass=str(cp)
            usr.set_password(npass)
            usr.save()
            subject='Password Changed'
            admin='bobadesp1234@gmail.com'
            msj=f'Hello {usr} , Your password is now change,Please save your new password for future and click on link for log in and enjoy the services Link:-http://127.0.0.1:8000/auth/login/ '
            send_mail(subject,msj,admin,[email],fail_silently=True)
            logout(request)
            return redirect('login')
        messages.error(request,'Please provide valid credentials')
    template_name='Auth/ChangePassword.html'
    return render(request,template_name)
