from django.db import models

# Create your models here.
from django.db import models

class Livro(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    resumo = models.TextField()
    linkimg = models.ImageField(upload_to='livros/')
    pdf = models.FileField(upload_to='livros/')
    nota = models.DecimalField(max_digits=3, decimal_places=1)
    sub_categoria = models.CharField(max_length=255, blank=True)  # Campo em branco, se necessário
    estoque = models.IntegerField(null=True)
    categoria = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.nome} - {self.id}'
