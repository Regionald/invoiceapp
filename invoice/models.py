from itertools import product
from sys import maxsize
from django.db import models

# Create your models here.

class User(models.Model):
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    companyName=models.CharField(max_length=100,default='No name')
    companyAddress=models.CharField(max_length=100,default='No address')
    town=models.CharField(max_length=50,default='no town')
    postalCode=models.IntegerField(default=1540)
    accountNumber=models.IntegerField(default=1541048928)
    logoName=models.CharField(max_length=100,default='logo')
    verified=models.BooleanField(default=False)

class Clients(models.Model):
    email = models.CharField(max_length=30)
    clientName = models.CharField(max_length=60)
    clientAddress = models.CharField(max_length=60)
    clientTown=models.CharField(max_length=100,default='No name')
    clientpostalCode=models.IntegerField(default=1540)
    products=models.JSONField()
    subTotal=models.IntegerField(default=0)
    vat=models.IntegerField(default=0)
    Total=models.IntegerField(default=0)
    