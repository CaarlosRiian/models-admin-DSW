from django.shortcuts import render, get_object_or_404
from .forms import FornecedorForm, CategoriaForm, ProdutoForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .models import Produto, Categoria, Fornecedor
from django.db.models import Q

# CBV teste

class ProdutoListView(ListView):
    model = Produto
    template_name = "produtos/index.html"
    context_object_name = "produtos"
    paginate_by = 6

    def get_queryset(self):
        queryset = Produto.objects.all()
        nome_busca = self.request.GET.get('nome', '')
        preco_min = self.request.GET.get('preco_min', '')
        preco_max = self.request.GET.get('preco_max', '')

        if nome_busca:
            queryset = queryset.filter(nome_produto__icontains=nome_busca) 

        if preco_min:
            queryset = queryset.filter(preco__gte=preco_min)
        if preco_max:
            queryset = queryset.filter(preco__lte=preco_max)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nome'] = self.request.GET.get('nome', '')
        context['preco_min'] = self.request.GET.get('preco_min', '')
        context['preco_max'] = self.request.GET.get('preco_max', '')
        return context

class CategoriaListView(ListView):
    model = Categoria
    template_name = "produtos/listar_categorias.html"
    context_object_name = "categorias"

class FornecedorListView(ListView):
    model = Fornecedor
    template_name = "produtos/listar_fornecedores.html"
    context_object_name = "fornecedores"

class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'detalhes_produtos.html'
    context_object_name = 'produtos'

class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'cadastrar_categoria.html'
    success_url = reverse_lazy('listar_categorias')

class FornecedorCreateView(CreateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = 'cadastrar_fornecedor.html'
    success_url = reverse_lazy('listar_fornecedores')

class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'cadastrar_produto.html'
    success_url = reverse_lazy('index')