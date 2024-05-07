from .views import *
from django.urls import path

app_name = 'mainapp'

urlpatterns = [
    path('log/', log, name='log'),
]
