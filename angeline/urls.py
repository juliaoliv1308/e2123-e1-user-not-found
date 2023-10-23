from django.contrib import admin
from django.urls import path, include
from .views import helloworld, pesquisar_livros, categ_livros, alugar_livro

app_name = 'angeline'

urlpatterns = [
    path('', helloworld, name='helloworld'),
    path('pesquisar/', pesquisar_livros, name='pesquisar_livros'),
    path('categlivros/<int:categ_id>/', categ_livros, name='categlivros'),
    path('alugar/<int:book_id>/', alugar_livro, name='alugar_livro'),
]
