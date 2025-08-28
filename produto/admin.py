from django.contrib import admin

from . import models

class VariacaoInline(admin.TabularInline):
    model = models.Varaiacao
    extra = 1
    
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome','get_preco_formatado', 'get_preco_formatado1']
    inlines = [VariacaoInline]
  

admin.site.register(models.Produto, ProdutoAdmin)
admin.site.register(models.Varaiacao)
