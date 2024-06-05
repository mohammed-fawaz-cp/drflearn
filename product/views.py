from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from . models import Product
from . productserializer import ProductSerializer
from rest_framework import generics

class ProductList(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer  
    def post(self, request, *args, **kwargs):
        return Response(self.create(request, *args, **kwargs).data)


