from django.contrib import admin
from django.urls import path, include
from .views import helloworld, pesquisar_livros, alugar_livro, categlivro

app_name = 'angeline'

urlpatterns = [
    path('', helloworld, name='helloworld'),
    path('pesquisar/', pesquisar_livros, name='pesquisar_livros'),
    path('alugar/<int:book_id>/', alugar_livro, name='alugar_livro'),
    path('categlivro/<int:categid>/', categlivro, name='categlivro'),
]
