from http import client
from django.shortcuts import render,redirect

#@descript /page after succeful loging
#@ GET /invoice/
client=[{'email' : 'regionald',
    'clientName' :'Reggy',
    'clientAddress':'50 maxixini',
    'clientTown':'Acornhoek',
    'clientpostalCode':1560,
    'products':[{'descript':'50 kg cement','rate':50,'qty':5,'ammout':250}],
    'subTotal':75,
    'vat':15,
    'Total':100
    }]

def invoice(request):
    return render(request,'invoice/invoice.html')

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
       qty=request.POST.getlist('qty')
       
       print(request.POST)
       print(len(descript))
  
    return redirect('/invoice/')

