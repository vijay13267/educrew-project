from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from datetime import datetime

from .models import *

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
                messages.info(request,'Username/Password is incorrect')
        context = {}
        return render(request,'educrew/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    #date and time info
    #user1=authenticate(request,username=username,password= password)
    person = request.user.username
    user = Student.objects.get(rollno=person)
    today = datetime.now()
    date = today.strftime("%d %B, %Y")
    day = today.strftime("%A")

    #schedule info
    schedule = StudentSchedule.objects.get(dept_id=1,sec=3,day='Friday')
    faculty = SubjectInfo.objects.get(unq_id=1000)
    context = {'user':user, 'date':date, 'day': day,
    'schedule':schedule,'faculty':faculty,
    }
    return render(request,'educrew/home.html',context)

@login_required(login_url='login')
def profile(request):
    person = request.user.username
    user = Student.objects.get(rollno=person)
    context = {'user':user}
    return render(request,'educrew/profile.html',context)

@login_required(login_url='login')
def explore(request):
    context = {}
    return render(request,'educrew/explore.html',context)
