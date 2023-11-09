from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import helloworld, pesquisar_livros, alugar_livro, categlivro, lista_alugados

app_name = 'angeline'

urlpatterns = [
    path('helloworld/', helloworld, name='helloworld'),
    path('pesquisar/', pesquisar_livros, name='pesquisar_livros'),
    path('pesquisar/<str:categ_id>/', pesquisar_livros, name='pesquisar_livros_por_categoria'),
    path('categlivros/<int:categ_id>/', categ_livros, name='categlivros'),
#   path('categ_livros/', categ_livros, name='categ_livros'),
    path('alugar/<int:book_id>/', alugar_livro, name='alugar_livro'),
    path('categlivro/<int:categid>/', categlivro, name='categlivro'),
    path('alugados/', lista_alugados, name='alugados'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.register, name='register'),
]

