from django.urls import path
from . import views
urlpatterns = [
    path('<int:pk>/',views.ProductList.as_view(),name='product' ),
    path('create/',views.ProductCreate.as_view(),name='productCreate1' ),
   
]