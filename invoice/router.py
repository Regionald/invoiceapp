from django.urls import path

from invoice import account
from . import login
from . import invoice

urlpatterns =[
    path('',login.landing,name='landing'),
    path('user/',login.user,name='user'),
    path('home/',login.home,name='home'),
    path('invoice/',invoice.invoice,name='get invoice'),
    path('invoice/create/',invoice.create,name='create invoice'),
    path('account/create/',account.createAcount,name='create account'),
    path('invoice/download/<int:id>/',invoice.download,name='download'),
]
