from django.urls import  path
from . import views

app_name = 'produto' #produto:lista


urlpatterns = [
    path('', views.ListaProdutos.as_view(), name='lista'),
    path('adicionarcarrinho/', views.AdicionarCarrinho.as_view(), name='adicionarcarrinho'),
    path('removercarrinho/', views.RemoverCarrinho.as_view(), name='removercarrinho'),
    path('carrinho/', views.Carrinho.as_view(), name='carrinho'),
    path('finalizar/', views.Finalizar.as_view(), name='finalizar'),
    path('<slug:slug>/', views.DetalheProduto.as_view(), name='detalhe')

]