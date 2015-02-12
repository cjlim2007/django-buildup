from django.http import HttpResponse
from django.shortcuts import render
def hello(request):
    return HttpResponse("Hello world!")

def hello_template(request, yourname):
    return HttpResponse("Hello {}".format(yourname))
