from django.urls import path
from app2.views import * 

name='app2'

urlpatterns=[
    path('html3/',html3,name='html3'),
    path('html4/',html4,name='html4'),
    path('msg/',msg,name='msg')
]