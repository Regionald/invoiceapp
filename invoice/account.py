from email import message
from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

#@descript create account
#@ POST /account/create

def createAcount(request):
 if request.method == 'POST':
       email=request.POST.get('email')
       password=request.POST.get('password')
       companyName=request.POST.get('companyName')
       companyAddress=request.POST.get('companyAddress')
       town=request.POST.get('town')
       postalCode=request.POST.get('postalCode')
       accountNumber=request.POST.get('accountNumber')
       #logoName=request.POST.get('')
       print(email)
       try : 
        print('Ínside try')
        user=User.objects.create(
        email=email,
        password=password,
        companyName=companyName,
        companyAddress=companyAddress,
        town=town,
        postalCode=postalCode,
        accountNumber=accountNumber
        )
        user.save()
       except:
           messages.error(request, 'Username OR password does not exit')

       return redirect('/')