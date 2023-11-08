from django.contrib import admin
from .models import Livro, Autor

# Register your models here.

admin.site.register(Livro)
admin.site.register(Autor)