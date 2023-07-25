from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def html5(request):
    return render(request,'html5.html')

def html6(request):
    return render(request,'html6.html')

def msg(request):
    return HttpResponse('<center><h1>app3 http response...🤗🤗🤗</h1></center>')