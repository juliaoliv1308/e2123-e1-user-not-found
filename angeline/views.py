from django.shortcuts import render
from .dicionarios import acao, suspense, romance, biografias, terror

# Create your views here.
def helloworld(request):
    novo_dicionario = {}

    for i in range(1, 7):
        novo_dicionario[str(i)] = {
            'nome': acao[str(i)]['nome'],
            'resumo': suspense[str(i)]['resumo'],
            'linkimg': romance[str(i)]['linkimg'],
            'pdf': biografias[str(i)]['pdf'],
            'nota': terror[str(i)]['nota']
        }

    # Exibindo o novo dicionário    
    print(novo_dicionario)

    context = {
        "novo_dic": novo_dicionario,
        'range_2': [0, 1],
        'range_3': [0, 1, 3]
    }
    return render(request, 'angeline/index.html', context)
 