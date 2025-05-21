from django.db import models
from order.models import Order
from product.models import Product

class OrderItem(models.Model):
    quantity = models.IntegerField("Quantidade")
    unitary_price = models.DecimalField("Preço Unitário", max_digits=10, decimal_places=2)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Item de Pedido"
        verbose_name_plural = "Itens de Pedido"
        ordering = ["id"]

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"
