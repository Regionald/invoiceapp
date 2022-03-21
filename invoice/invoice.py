from copyreg import clear_extension_cache
import datetime
from email.policy import HTTP
from pickle import TRUE
from pickletools import read_bytes4
from re import sub
from django.shortcuts import render,redirect
import operator
from invoice.models import Clients
from django.contrib import messages
from django.http import HttpResponse
import os
os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\bin")
os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\lib\girepository-1.0")
#from weasyprint import HTML
import tempfile
from django.template.loader import render_to_string


#@descript /page after succeful loging
#@ GET /invoice/

def invoice(request):
    client=Clients.objects.filter(email='regionaldmongwe@gmail.com').values()
    return render(request,'invoice/invoice.html',{'client':client})

#@descript /create invoice 
#@ GET /invoice/create
def create(request):
    if request.method == 'POST':
       clientName=request.POST.get('name')
       clientAddress=request.POST.get('address')
       clientTown=request.POST.get('town')
       clientpostalCode=request.POST.get('code')
       descript=request.POST.getlist('descript')
       rate=request.POST.getlist('rate')
       dueDate=request.POST.getlist('dueDate')
       qty=request.POST.getlist('qty')
       
       rate=[int(i) for i in rate]
       qty=[int(i) for i in qty]
       
       amount=list(map(operator.mul,rate,qty))
       products=[{'descpript': descript, 'rate': rate,'qty':qty,'amount':amount} for descript, rate,qty,amount in zip(descript, rate,qty,amount)]
       total=sum(amount)
       subTotal=0
       vat=0
       if request.POST.get('typeOFinvoice')=='Tax invoice':
        subTotal=round(0.85*total,2)
        vat=round(0.15*total,2)
       try :
         user=Clients.objects.create(
         email='regionaldmongwe@gmail.com',
         clientName = clientName,
         clientAddress =clientAddress,
         clientTown=clientTown,
         clientpostalCode=clientpostalCode,
         products=products,
        # dueDate=dueDate,
         #date=datetime.now(),
         subTotal=subTotal,
         vat=vat,
         Total=total,)
       except:
        messages.error(request, 'Username OR password does not exit')
    return redirect('/invoice/')

def download(request,id):
  invoice=Clients.objects.filter(id=id).values()
  print(invoice)
  return render(request,'invoice/download.html',{'client':invoice})





















# source codes weasy print
 #'''response=HttpResponse(content_type='application/pdf')
 #  response['Content-Disposition']='attachement;filename'+\
 #   str(datetime.datetime.now())+'.pdf'
 #  response['Content-Transfer-Encoding']='binary'
 # html_string=render_to_string('invoice/download.html')
  #html=HTML(string=html_string)
  #result=html.write_pdf()

  #with tempfile.NamedTemporaryFile(delete=True) as output:
  #  output.write(result)
  #  output.flush()
  # output=open(output.name,'rb')
  #  response.write(output.read())
  #return response''' 

