from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from .views import helloworld, books
=======
from .views import helloworld, pesquisar_livros
>>>>>>> 4828a441a843750052ecbade9992b9c86b078408

app_name = 'angeline'

urlpatterns = [
    path('', helloworld, name='helloworld'),
<<<<<<< HEAD
    path('books', books, name='books')
=======
    path('pesquisar/', pesquisar_livros, name='pesquisar_livros'),
>>>>>>> 4828a441a843750052ecbade9992b9c86b078408
]