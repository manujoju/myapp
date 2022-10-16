
from multiprocessing import context
from pydoc import render_doc
from django.shortcuts import HttpResponse
from django.shortcuts import render

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