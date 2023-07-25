from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def html1(request):
    return render(request,'html1.html')

def html2(request):
    return render(request,'html2.html')

def msg(request):
    return HttpResponse('<center><h1>This is app1 http responce...😜😜😜😜</h1><center>')