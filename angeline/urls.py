from django.contrib import admin
from django.urls import path, include
from .views import helloworld

app_name = 'main'

urlpatterns = [
    path('', helloworld, name='helloworld'),
]