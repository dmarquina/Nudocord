from django.db import models
from products.models import Product

class Ordersdetail():
	product = models.ForeignKey(Product, verbose_name='producto')
	order = models.ForeignKey(Pedido, verbose_name='pedido')
	 = models.PositiveIntegerField(verbose_name='cantidad')