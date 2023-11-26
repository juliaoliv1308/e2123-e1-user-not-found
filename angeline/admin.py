from django.contrib import admin
from .models import Livro, Editora, Autor, Status, Avaliacao_usuario
# Register your models here.

admin.site.register(Autor)
admin.site.register(Status)
admin.site.register(Editora)
admin.site.register(Avaliacao_usuario)


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nota_media_display')
    readonly_fields = ('nota_media_display',)

    def nota_media_display(self, obj):
        return obj.nota_media
    nota_media_display.short_description = 'Nota Média'

