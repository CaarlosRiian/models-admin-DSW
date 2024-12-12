from django.shortcuts import render
from .models import Produto

def index(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos
        
        }
    return render(request, 'index.html', context)

def detalhes(request, pk):
    detalhes_produto = Produto.objects.get(id=pk)
    context = {
        'produtos': detalhes_produto 
    }
    return render(request, 'detalhes_produtos.html', context)
