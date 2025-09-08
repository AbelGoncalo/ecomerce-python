from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from . import  models


class ListaProdutos(ListView):
        model = models.Produto
        template_name = 'produto/lista.html'    
class DetalheProduto(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhe do carrinho')

class AdicionarCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Adiconar ao carrinho')
class RemoverCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Remover')

class Carrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Carrinho')

class Finalizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finalizar carrinho')



# Create your Views here.
