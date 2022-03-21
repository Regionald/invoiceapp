from itertools import product
from sys import maxsize
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    companyName=models.CharField(max_length=100,default='No name')
    companyAddress=models.CharField(max_length=100,default='No address')
    town=models.CharField(max_length=50,default='no town')
    postalCode=models.IntegerField(default=1540)
    accountNumber=models.IntegerField(default=1541048928)
    logoName=models.CharField(max_length=100,default='logo')
    verified=models.BooleanField(default=False)

class Clients(models.Model):
    email = models.CharField(max_length=30,)
    clientName = models.CharField(max_length=60,default='No name')
    clientAddress = models.CharField(max_length=60,default='No name')
    clientTown=models.CharField(max_length=100,default='No name')
    clientpostalCode=models.IntegerField(default=1540)
    products=models.JSONField(default=dict)
    subTotal=models.IntegerField(default=0)
    vat=models.IntegerField(default=0)
    Total=models.IntegerField(default=0)

#dueDate=models.CharField(max_length=60,null=True,blank=True)
#createDate=models.CharField(max_length=60,null=True,blank=True)   