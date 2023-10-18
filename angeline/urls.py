from django.contrib import admin
from django.urls import path, include
from .views import helloworld, books

app_name = 'angeline'

urlpatterns = [
    path('', helloworld, name='helloworld'),
    path('books', books, name='books')
]