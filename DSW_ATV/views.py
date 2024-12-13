from django.shortcuts import render, get_object_or_404
from .models import *

def index(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos
        
        }
    return render(request, 'index.html', context)

def detalhes(request, pk):
    detalhes_produto = get_object_or_404(Produto, id=pk)
    context = {
        'produtos': detalhes_produto 
    }
    return render(request, 'detalhes_produtos.html', context)


def listar_categorias(request):
    categorias = Categoria.objects.all()
    context = {'categorias': categorias}
    return render(request, 'listar_categorias.html', context)

def listar_fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    context = {'fornecedores': fornecedores}
    return render(request, 'listar_fornecedores.html', context)

