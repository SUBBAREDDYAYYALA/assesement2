from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def html3(request):
    return render(request,'html3.html')

def html4(request):
    return render(request,'html4.html')

def msg(request):
    return HttpResponse('<center><h1>app http response...🥴🥴🥴🥴</h1></center>')