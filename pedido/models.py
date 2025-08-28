from django.db import models
from django.contrib.auth.models import User

class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()
    status = models.CharField(
        default='C',
        max_length=1, 
        choices=(
            ('A', 'Aprovado'),
            ('C', 'Criado'),
            ('R', 'Reprovado'),
            ('P', 'Pendente'),
            ('E', 'Enviado'),
            ('F', 'Finalizado'),
         ) 
        )
 
    def __str__(self):
        return f'Pedido n: {self.id}  - {self.get_status_display()}'


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.CharField(max_length=255)
    produto_id = models.PositiveBigIntegerField()
    variacao = models.CharField(max_length=255, blank=True, null=True)
    variacao_id = models.PositiveIntegerField (blank=True, null=True)
    preco = models.FloatField()
    preco_promocional = models.FloatField(default=0)
    quantidade = models.IntegerField()
    imagem = models.CharField(max_length=2000, blank=True, null=True)
    
    def __str__(self):
        return f'Item {self.id} - Pedido {self.pedido.id} - {self.produto}'
 

class Meta:
    verbose_name = 'Item do Pedido'
    verbose_name_plural = 'Itens do Pedido'