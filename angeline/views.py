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

meio = len(dicionarios) // 2

# Divide o dicionário em duas partes
dict1 = dict(list(dicionarios.items())[:meio])
dict2 = dict(list(dicionarios.items())[meio:])


def helloworld(request):
    notas_maximas1 = melhores(dict1)
    notas_maximas2 = melhores(dict2)
    print(notas_maximas1, notas_maximas2)

    context = {
        "novo_dic1": notas_maximas1,
        "novo_dic2": notas_maximas2,
    }
    return render(request, 'angeline/index.html', context)




