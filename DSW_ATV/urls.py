from django.urls import path
from DSW_ATV import views
from DSW_ATV.views import ProdutoListView, CategoriaListView, FornecedorCreateView, ProdutoDetailView, CategoriaCreateView, ProdutoCreateView

urlpatterns = [
    path('', views.ProdutoListView.as_view(), name='index'),
    path('<int:question_id>', views.ProdutoDetailView.as_view(), name='detail'),
    path('categorias/', views.CategoriaListView.as_view(), name='listar_categorias'),
    path('fornecedores/', views.FornecedorListView.as_view(), name='listar_fornecedores'),
    path('cadastrar_fornecedor/', views.FornecedorCreateView.as_view(), name='cadastrar_fornecedores'),
    path('cadastrar_categoria/', views.CategoriaCreateView.as_view(), name='cadastrar_categoria'),
    path('cadastrar_produtos/', views.ProdutoCreateView.as_view(), name='cadastrar_produto'),
]
