from django.urls import path
from DSW_ATV import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>', views.detalhes, name='details'),
    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('fornecedores/', views.listar_fornecedores, name='listar_fornecedores'),
]

