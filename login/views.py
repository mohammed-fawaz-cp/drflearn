from django.shortcuts import render

from django.forms.models import model_to_dict
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Login
from .loginserializers import LoginSerializer

@api_view(['GET','POST'])
def login_create(request,*args,**kwargs):
    instance = Login.objects.all().order_by("?")
    
    data=LoginSerializer(instance,many = True).data
    return Response(data)

@api_view(['POST'])
#create a function to accept data from user
def login_getdata(request,*args,**kwargs):
    if request.method == 'POST':
        data = request.data
        print(data)
        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)