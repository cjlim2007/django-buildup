from datetime import datetime
from random import randint
import subprocess
from django.shortcuts import render



    
def hello_template(request, yourname, yoursentence):
    subprocess.call(["say", yoursentence])
    return render(request, "hello.html", { "yourname": yourname, "foobar": 12, "time": (datetime.now()), "random": randint(1,10)})
