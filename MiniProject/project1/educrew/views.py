from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else :
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user=authenticate(request,username=username,password= password)
            if user is not None :
                login(request, user)
                return redirect('home') 
            else:
                messages.info(request,'username/password is incorrect')
        context = {}
        return render(request,'educrew/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    context = {}
    return render(request,'educrew/home.html',context)

@login_required(login_url='login')
def profile(request):
    context = {}
    return render(request,'educrew/profile.html',context)

@login_required(login_url='login')
def explore(request):
    context = {}
    return render(request,'educrew/explore.html',context)
