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
    path('account/create/',account.createUserAccount,name='create account now'),
    path('invoice/download/<int:id>/',invoice.download,name='download'),
    path('invoice/delete/<int:id>/',invoice.delete,name='delete invoice'),
    path('invoice/email/<int:id>/',invoice.sendEmail,name='send invoice'),
    path('invoice/edit/<int:id>/',invoice.editInvoice,name='edit invoice'),
    path('invoice/copy/<int:id>/',invoice.copy,name='copy invoice'),
    path('invoice/logout/',login.logOut,name='logOut'),
    path('invoice/profile/',account.profile,name='display the edit html'),
    path('account/update/',account.profileUpdate,name='update account now'),
    path('account/upload/',account.picUpload,name='upload a new picture now'),
]
