from django.contrib import admin
from .models import Categoria, Aluguel, Livro


admin.site.register(Categoria)
admin.site.register(Aluguel)
admin.site.register(Livro)