
from multiprocessing import context
from pydoc import render_doc
from django.shortcuts import HttpResponse
from django.shortcuts import render

from myapp.models import product

# Create your views here.
def index(request):
    d = {
        "name":"arun",
        "age":30,
    }
    li = ["manu","ar","max"]
    
    for i in range(0,10):
        print (i)
    context ={'li':li}
        
    return render (request, 'index.html',context=context)

def new_one(request):
    return HttpResponse("this is new")

def products(request):
    p = product.objects.all()
    context = {'products':p}
    return render(request, 'myapp/products.html',context=context)

def product_details(request,id):
    p = product.objects.get(id=id)
    context={'p':p}
    return render (request,'myapp/product_details.html',context=context)

def add_product(request):
    p = product(name="samsung 32 inch monitor",price=36000.0)
    p.description = "this hd monitor"
    p.save()
    return HttpResponse(p)