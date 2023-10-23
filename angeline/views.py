from django.shortcuts import render
from .dicionarios import dicionarios
import unicodedata

# Create your views here.


def melhores(dicionarios):
    notas_maximas = {}
    for categoria, dicionario in dicionarios.items():
        nota_maxima = None
        livro_maximo = None
        for chave, valor in dicionario.items():
            if nota_maxima is None or valor["nota"] > nota_maxima:
                nota_maxima = valor["nota"]
                livro_maximo = valor
        notas_maximas[categoria] = livro_maximo
    return notas_maximas


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
        caracter_sem_acento = unicodedata.normalize('NFD', caracter).encode('ascii', 'ignore').decode('utf-8')
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
    meio = len(dicionarios) // 2

    # Divide o dicionário em duas partes
    dict1 = dict(list(dicionarios.items())[:meio])
    dict2 = dict(list(dicionarios.items())[meio:])
        
    notas_maximas1 = melhores(dict1)
    notas_maximas2 = melhores(dict2)

    context = {
        "novo_dic1": notas_maximas1,
        "novo_dic2": notas_maximas2,
    }
    return render(request, 'angeline/index.html', context)


def books(request, book_id):
    livros_encontrados = {}
    
    for categoria, lista_livros in dicionarios.items():
        for id, livro in lista_livros.items():
            if livro["id"] == book_id:
                livro["categoria"] = categoria
                livros_encontrados[categoria] = livro

    # Inicialize as variáveis fora do loop e remova o segundo loop
    categoriaf = None
    livrof = None

    for c, l in livros_encontrados.items():
        categoriaf = c
        livrof = l
    
    context = {
        'livro': livrof,
        'categoria': categoriaf,
    }
    print(livros_encontrados)
    
    return render(request, 'angeline/books.html', context)


def categ_livros(request, categ_id):
    for categoria, dicionario in dicionarios.items():
        for chave, valor in dicionario.items():
            pass






    return render(request, 'angeline/categlivros.html')
