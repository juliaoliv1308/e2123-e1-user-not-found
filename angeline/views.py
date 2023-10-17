from django.shortcuts import render
from .dicionarios import acao, suspense, romance, biografias, terror, ficcao

# Create your views here.

def melhores(dicionarios):
    notas_maximas = {}
    for categoria, dicionario in dicionarios.items():
        nota_maxima = max(dicionario, key=lambda k: dicionario[k]["nota"])
        notas_maximas[categoria] = dicionario[nota_maxima]
    
    return notas_maximas

dicionarios = {
    "Ação": acao,
    "Suspense": suspense,
    "Romance": romance,
    "Biografias": biografias,
    "Terror": terror,
    "Ficção Científica": ficcao,
}

def helloworld(request):
    novo_dicionario = {}

    # Calcule as notas mais altas
    notas_maximas = melhores(dicionarios)
    print(notas_maximas)

    context = {
        "novo_dic": novo_dicionario,
        'range_2': [0, 1],
        'range_3': [0, 1, 3]
    }
    return render(request, 'angeline/index.html', context)




