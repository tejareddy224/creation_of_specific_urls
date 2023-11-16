from django.urls import path
from .views import *

app_name='teja'

urlpatterns=[
    path('kohli/',kohli,name='kohli'),
    path('abd/',abd,name='abd'),
]
