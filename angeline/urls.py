from django.contrib import admin
from django.urls import path, include
from .views import helloworld, pesquisar_livros

app_name = 'angeline'

urlpatterns = [
    path('', helloworld, name='helloworld'),
    path('pesquisar/', pesquisar_livros, name='pesquisar_livros'),
]