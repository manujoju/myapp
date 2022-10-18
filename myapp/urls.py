
from django.urls import path, include

from myapp.views import index
from. views import index, new_one, products

urlpatterns = [
    path('',index),
    path('new',new_one),
    path('products',products)
]