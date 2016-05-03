from django.db import models
from orders.models import Order
from products.models import Product

class Ordersdetail(models.Model):
	quantity = models.IntegerField(verbose_name='cantidad')
	subtotal_price = models.DecimalField(max_digits=6, decimal_places=2,verbose_name='subtotal');
	order = models.ForeignKey(Order,verbose_name='pedido')
	product = models.ForeignKey(Product,verbose_name='producto')

	def __str__(self):
		return '%s' % (self.product.name)

	class Meta:
		ordering = ('id',)

