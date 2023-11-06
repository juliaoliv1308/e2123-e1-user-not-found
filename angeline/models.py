from django.db import models

# Create your models here.
from django.db import models


class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, verbose_name='Author name', null=True)

    def __str__(self):
        return self.nome

class Editora(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, verbose_name='Publisher name', null=True)
    livro_nome = models.CharField(max_length=255, verbose_name='Book title', null=True)

class Status(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.BooleanField(default=False)

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
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, verbose_name='Author', null=True)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE, verbose_name='Publisher', null=True)

    def __str__(self):
        return f'{self.nome} - {self.id}'

