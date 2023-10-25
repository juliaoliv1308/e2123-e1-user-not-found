from django.contrib import admin
from django.urls import path, include
from .views import helloworld, pesquisar_livros, alugar_livro, categ_livros

app_name = 'angeline'

urlpatterns = [
    path('', helloworld, name='helloworld'),
    path('pesquisar/', pesquisar_livros, name='pesquisar_livros'),
    path('pesquisar/<str:categ_id>/', pesquisar_livros, name='pesquisar_livros_por_categoria'),
    path('categlivros/<int:categ_id>/', categ_livros, name='categlivros'),
#   path('categ_livros/', categ_livros, name='categ_livros'),
    path('alugar/<int:book_id>/', alugar_livro, name='alugar_livro'),
]

