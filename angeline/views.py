from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .dicionarios import dicionarios, alugados
from .models import Livro
import unicodedata

# Create your views here.


def remover_acentos(texto):
    # Passo 1: Transformar o texto em minúsculas
    texto = texto.lower()

    # Passo 2: Remover espaços em branco
    texto_sem_espacos = ""
    for caracter in texto:
        if caracter != " ":
            texto_sem_espacos += caracter

    # Passo 3: Remover acentos
    texto_sem_acentos = ""
    for caracter in texto_sem_espacos:
        caracter_sem_acento = unicodedata.normalize(
            'NFD', caracter).encode('ascii', 'ignore').decode('utf-8')
        texto_sem_acentos += caracter_sem_acento

    return texto_sem_acentos


def pesquisar_livros(request):
    query = request.GET.get('meuCampoDeTexto', '').strip()

    # Aplicar as transformações na string query
    query = remover_acentos(query)

    resultados = {}

    for categoria, dicionario in dicionarios.items():
        livros_correspondentes = {}
        for chave, valor in dicionario.items():
            # Aplicar as transformações na string valor["nome"]
            if valor["nome"]:
                nome_livro = remover_acentos(valor["nome"])
                if query in nome_livro.lower():
                    livros_correspondentes[chave] = valor

        if livros_correspondentes:
            resultados[categoria] = livros_correspondentes

    context = {
        "resultados": resultados,
    }
    return render(request, 'angeline/resultados_pesquisa.html', context)


def helloworld(request):
    # Obtém as melhores notas por categoria
    melhores_notas = Livro.melhores_notas_por_categoria()

    # Divide as categorias em duas partes
    meio = len(melhores_notas) // 2
    dict1 = dict(list(melhores_notas.items())[:meio])
    dict2 = dict(list(melhores_notas.items())[meio:])

    resultados = {}

    for categoria, dicionario in dicionarios.items():
        livros_correspondentes = {}
        if livros_correspondentes:
            resultados[categoria] = livros_correspondentes

    context = {
        "novo_dic1": dict1,
        "novo_dic2": dict2,
        "resultados": resultados,
    }
    return render(request, 'angeline/index.html', context)


@login_required
def alugar_livro(request, book_id):
    user = request.user
    livro_alugado = {}

    for categoria, dicionario in dicionarios.items():
        for chave, valor in dicionario.items():
            if valor["id"] == book_id:
                if request.method == 'POST':
                    if "button_alugar" in request.POST:

                        alugados[chave] = {"id": user.id, "valor": valor}
                        print(alugados)
                        if valor["estoque"] >= 1:
                            valor["estoque"] -= 1
                    elif "button_devolver" in request.POST:
                        if valor["estoque"] == 0:
                            valor["estoque"] += 1
                valor["categoria"] = categoria
                livro_alugado[categoria] = valor
                break  # Saia do loop interno, pois o livro foi encontrado

    # Inicialize as variáveis fora do loop e remova o segundo loop
    categoriaf = None
    livrof = None

    for c, l in livro_alugado.items():
        categoriaf = c
        livrof = l

    context = {
        'livro': livrof,
        'categoria': categoriaf,
    }

    return render(request, 'angeline/books.html', context)


@login_required
def lista_alugados(request):
    user = request.user  # Obtém o usuário atual

    context = {
        'user': user,
        'alugados': alugados,
    }

    return render(request, 'angeline/alugados.html', context)


def categlivro(request, categid):
    resultados = {}

    for categoria, dicionario in dicionarios.items():
        livros_correspondentes = {}
        for chave, valor in dicionario.items():
            if categid == valor["categoria"]:
                livros_correspondentes[chave] = valor

        if livros_correspondentes:
            resultados[categoria] = livros_correspondentes

    context = {
        "resultados": resultados,
    }
    return render(request, 'angeline/categlivros.html', context)


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Faça o login do usuário após o registro
            return redirect('helloworld/')  # Redirecione para a página de perfil após o registro
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form
    }

    return render(request, 'registration/register.html', context)
