
from django.urls import path, include

from myapp.views import index
from. views import index, new_one, products,product_details,add_product

urlpatterns = [
    path('',index),
    path('new',new_one),
    path('products',products),
    path('products/<int:id>',product_details),
    path('add_product/',add_product)
]