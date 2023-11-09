from django.db import models

# Create your models here.
from django.db import models


class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, verbose_name='Nome Autor', null=True, blank=True)

    def __str__(self):
        # Retorna o nome do autor e o ID em um formato string.
        return f"{self.nome} {self.id}"

    class Meta:
        # Define a ordenação padrão para ser pelo nome.
        ordering = ['nome']

        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

class Editora(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, verbose_name='Nome Editora', null=True)
    livro_nome = models.CharField(max_length=255, verbose_name='Titulo Livro', null=True)

    def __str__(self):
        # Retorna o nome do autor e o ID em um formato string.
        return f"{self.nome} {self.id}"

    class Meta:
        # Define a ordenação padrão para ser pelo nome.
        ordering = ['nome']

        verbose_name = 'Editora'
        verbose_name_plural = 'Editoras'

class Status(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.BooleanField(default=False, null=True)

    def __str__(self):
        # Retorna o nome do autor e o ID em um formato string.
        return f"{self.status} - {self.id}"

    class Meta:
        # Define a ordenação padrão para ser pelo nome.
        ordering = ['id']

        verbose_name = 'Statu'
        verbose_name_plural = 'Status'

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
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, verbose_name='Autor', null=True)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE, verbose_name='Editora', null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Status', null=True)

    def __str__(self):
        return f'{self.nome} - {self.id}'

    class Meta:
        # Define a ordenação padrão para ser pelo nome.
        ordering = ['nome']

        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'