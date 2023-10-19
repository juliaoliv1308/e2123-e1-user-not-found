from django.contrib import admin
from django.urls import path, include
from .views import helloworld, books, pesquisar_livros

app_name = 'angeline'

urlpatterns = [
    path('', helloworld, name='helloworld'),
    path('books', books, name='books'),
    path('pesquisar/', pesquisar_livros, name='pesquisar_livros'),
]