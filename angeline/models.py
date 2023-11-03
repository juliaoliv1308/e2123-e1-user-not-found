from django.db import models
from django.views.decorators.csrf import csrf_exempt


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    @csrf_exempt
    def __str__(self):
        return self.nome

class Aluguel(models.Model):
    status = models.CharField(max_length=100, default="")
    data_aluguel = models.DateTimeField(auto_now_add=True)
    data_devolucao = models.DateTimeField()

    @csrf_exempt
    def __str__(self):
        return f"Aluguel #{self.id}"
       


class Livro(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    resumo = models.TextField()
    linkimg = models.ImageField(upload_to='livros/')
    pdf = models.FileField(upload_to='livros/')
    nota = models.DecimalField(max_digits=3, decimal_places=1)
    sub_categoria = models.CharField(max_length=255, blank=True)
    estoque = models.PositiveIntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    aluguel = models.ForeignKey(Aluguel, on_delete=models.CASCADE, null=True)

    @csrf_exempt
    def __str__(self):
        return self.nome