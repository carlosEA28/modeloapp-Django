from django.db import models
from clients.models import Client

# # Create your models here.

class Order(models.Model):
    total_price = models.FloatField('Preco Total', null=True, blank=True, default=0.0)
    STATUS_CHOICES = (
        ('Em andamento', 'Em andamento'),
        ('Finalizado', 'Finalizado'),
        ('Cancelado', 'Cancelado'),
    )
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, null=True, blank=True, default='Em andamento')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    #created_on = models.DateTimeField(auto_now_add=True) | Usa horario atual para preencher campo
    
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering =['-client__id']
        #ordering =['created_on'] | Opcao usando para ordernar por hora.

    def __str__(self):
        return "%s" % (self.total_price) 