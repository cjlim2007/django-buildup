from datetime import datetime
from django.http import HttpResponse
def hello(request):
    return HttpResponse("Hello world!")

def time(request):
    return HttpResponse("The time is " + str(datetime.now()))