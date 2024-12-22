from django.urls import path
from .views import *

app_name='LinkAnchor'

urlpatterns=[
    path('',company,name='company'),
    path('online/',online,name='online'),
    path('offline/',offline,name='offline'),
]