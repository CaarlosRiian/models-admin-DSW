from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuestionForm, FornecedorForm, CategoriaForm, ProdutoForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Produto, Categoria, Fornecedor

# CBV teste

class ProdutoListView(ListView):
    model = Produto
    template_name = "produtos/index.html"
    context_object_name = "produto"

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