from datetime import datetime
from random import randint
import subprocess

from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello world!")

def time(request):
    return render(request, "time.html", { "current_time": str(datetime.now()) })

def random(request):
    return render(request, "random.html", { "random_number": randint(0, 10) })

def hello_template(request, yourname):
    return render(request, "hello.html", { "yourname": yourname, "foobar": 12 })

def speak(request, sentence):
    subprocess.call(["say", sentence])
    return render(request, "speak.html")
