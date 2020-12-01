from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.template import RequestContext
from .models import *

# Create your views here.

def index(request):
    return render(request,'index.html',{'name':(request.user.first_name)})
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html',{'message':'invalid credentials'})
    else:
        return render(request,'login.html')
def home(request):
    return render(request,'home.html',{'name':(request.user.first_name)})
def schedule(request):
    sch=Schedule.objects.all()
    jn=Join.objects.all()
    stu=Student.objects.all()
    return render(request,'schedule.html',{'name':(request.user.first_name),'auth':(request.user.username),'date':sch,'join':jn,'st':stu})
def profile(request):
    stu=Student.objects.all()
    return render(request,'profile.html',{'name':(request.user.first_name),'auth':(request.user.username),'prof':stu})
def logout(request):
    return render(request,'logout.html')
def allocate(request):
    alct=Allot.objects.all()
    sch=Schedule.objects.all()
    return render(request,'allocate.html',{'name':(request.user.first_name),'alloc':alct,'date':sch,'auth':(request.user.username)})
