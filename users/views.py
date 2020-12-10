from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def signin(request):
    if request.method =='POST':
        if request.POST['Password1'] == request.POST['Password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'users/signin.html',{'error':'This user has already been taken'})
            except User.DoesNotExist:
                user =  User.objects.create_user(request.POST['username'],password=request.POST['Password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'users/signin.html', {'error': 'Password dosent match'})
    else:
        return render(request, 'users/signin.html')

def login(request):
    if request.method =='POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request, 'users/login.html', {'error': 'The user or password incorrect'})
    else:
        return render(request, 'users/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

    else:
        return render(request, 'users/logout.html')