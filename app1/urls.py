from django.urls import path
from app1.views import *
 
app='app1'

urlpatterns=[
    path('html1/',html1,name='html1'),
    path('html2/',html2,name='html2'),
    path('msg/',msg,name='msg')
]