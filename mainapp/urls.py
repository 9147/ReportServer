from .views import *
from django.urls import path

app_name = 'mainapp'

urlpatterns = [
    path('', home, name='home'),
    path('data/', data_api, name='data'),
    path('login/', login_api, name='login'),
]
