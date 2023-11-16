from django.urls import path

from mi.views import *

app_name='teja'

urlpatterns=[

    path('rohit/',rohit,name='rohit'),
    
]