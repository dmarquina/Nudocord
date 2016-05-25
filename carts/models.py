from django.db import models
from products.models import Product
from clients.models import Client

class Cart(models.Model):
	quantity = models.IntegerField(verbose_name='cantidad')
	subtotal_amount = models.DecimalField(max_digits=6,decimal_places=2,verbose_name='subtotal')
	product = models.ForeignKey(Product,verbose_name='producto',null=True)
	client = models.ForeignKey(Client,null=True,verbose_name='cliente')

	def __str__(self):
		return '%s' % (self.product.name)

	class Meta:
		ordering = ('id',)

