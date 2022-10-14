
from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    d = {
        "name":"arun",
        "age":30,
    }
    return HttpResponse("<b>hello world</b>")