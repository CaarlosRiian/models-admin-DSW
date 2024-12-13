from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Produto)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('cod_produto', 'nome_produto', 'preco', 'qntd_estoque', 'data_criacao')
    search_fields = ('cod_produto', 'nome')
    ordering = ('-data_criacao',)

admin.site.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('cod_categoria', 'nome_categoria')

    ordering = ('-data_criacao',)
    
admin.site.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('cod_fornecedor','nome_fornecedor')
