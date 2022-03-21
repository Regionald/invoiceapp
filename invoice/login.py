from asyncio.windows_events import NULL
from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your views here.
#@descript login/landing page
#@ GET /
def landing(request):
    print(request)
    return render(request,'invoice/login.html')


#@descript login userName and password Validation
#@ Post /user

def user(request):
    if request.method == 'POST':
       email=request.POST.get('email')
       password=request.POST.get('password')
       #user=User.objects.filter(email=email).first()
       try:
        user=User.objects.get(email=email,password=password)
        print(1,user)
       except:
        messages.error(request, 'Username OR password does not exit')

       user=authenticate(request,email=email,password=password) 
       print(3,user)
       if user is not None:
           login(request,user)
           print('print is not None')
           return redirect('/home/')
    print(email,password)
    return redirect('/')




#@descript /page after succeful loging
#@ GET /invoice/
def home(request):
    return render(request,'invoice/index.html')

