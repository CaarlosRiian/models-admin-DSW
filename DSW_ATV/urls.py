from django.urls import path
from DSW_ATV import views
from DSW_ATV.views import ProdutoListView, CategoriaListView, FornecedorCreateView, FornecedorListView, ProdutoDetailView, CategoriaCreateView, ProdutoCreateView, LogoutView, LoginView, UserRegisterView

urlpatterns = [
    path('', ProdutoListView.as_view(), name='index'),
    path('<int:question_id>', ProdutoDetailView.as_view(), name='detail'),
    path('categorias/', CategoriaListView.as_view(), name='listar_categorias'),
    path('fornecedores/', FornecedorListView.as_view(), name='listar_fornecedores'),
    path('cadastrar_fornecedor/', FornecedorCreateView.as_view(), name='cadastrar_fornecedores'),
    path('cadastrar_categoria/', CategoriaCreateView.as_view(), name='cadastrar_categoria'),
    path('cadastrar_produtos/', ProdutoCreateView.as_view(), name='cadastrar_produto'),

    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
]
