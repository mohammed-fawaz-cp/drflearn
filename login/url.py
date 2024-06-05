from django.contrib import admin
from django.urls import path,include
from .views import login_create,login_getdata
urlpatterns = [
    path('',login_create,name='login1' ),
    path('login/',login_getdata,name='login2')
    
]