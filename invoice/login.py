from asyncio.windows_events import NULL
from django.shortcuts import render, redirect
#from .models import User

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
      # user=User.objects.create(
       #email=email,
       #password=password,
      # )
    print(email,password)
    return redirect('/home/')

#@descript /page after succeful loging
#@ GET /invoice/
def home(request):
    return render(request,'invoice/index.html')

