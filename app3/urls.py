from django.urls import path
from app3.views import *

app='app3'

urlpatterns=[
    path('html5/',html5,name='hmtl5'),
    path('html6/',html6,name='html6'),
    path('msg/',msg,name='msg')
]