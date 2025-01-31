from django.urls import path
from DSW_ATV import views
from DSW_ATV.views import ProdutoListView, CategoriaListView, FornecedorListView

urlpatterns = [
    path('', views.ProdutoListView.as_view(), name='index'),
    path('<int:question_id>', views.detalhes, name='detail'),
    path('categorias/', views.CategoriaListView.as_view(), name='listar_categorias'),
    path('fornecedores/', views.FornecedorListView.as_view(), name='listar_fornecedores'),
    path('cadastrar_fornecedor/', views.cadastrar_fornecedor, name='cadastrar_fornecedores'),
    path('cadastrar_categoria/', views.cadastrar_categoria, name='cadastrar_categoria'),
    path('cadastrar_produtos/', views.cadastrar_produtos, name='cadastrar_produto'),
]
