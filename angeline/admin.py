from django.contrib import admin
from .models import Livro, Editora, Autor, Status

# Register your models here.

admin.site.register(Livro)
admin.site.register(Autor)
admin.site.register(Status)
admin.site.register(Editora)
