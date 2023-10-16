from django.shortcuts import render

# Create your views here.
def helloworld(request):
    for id_livro, info in principal.items():
        id_fornecedor = info['codigo_fornecedor']
        fornecedor_info = fornecedores.get(id_fornecedor, "ID não encontrado")

        
        if fornecedor_info and categoria_info != "ID não encontrado":
            lista_fusão[id_livro] = {
                'nome': info['nome'],
            }
            media = media + info['diasvencidos']
        else:
            lista_fusão[id_livro] = {
                'nome': info['nome'],
            }

    context = {

    }
    return render(request, 'angeline/index.html')

 