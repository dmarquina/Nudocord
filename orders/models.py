from django.db import models
from clients.models import Client
from deliverplaces.models import Deliverplace
from products.models import Product

class Order(models.Model):
	STATES_CHOICES = (
		('PR', 'En Proceso'),
		('EN', 'Entregado'),
		('CA', 'Cancelado'),
	)
	state = models.CharField(max_length=2,verbose_name='estado',choices=STATES_CHOICES)
	amount	= models.DecimalField(max_digits=6, decimal_places=2, verbose_name='precio total')
	registration_date = models.DateField(auto_now=False, auto_now_add=True, verbose_name='fecha de registro',blank=True)	
	client = models.ForeignKey(Client, verbose_name='cliente')
	deliverplace = models.ForeignKey(Deliverplace, verbose_name='lugar de entrega')

	def __str__(self):
		return '%s' % (self.client.userprofile.name)

	class Meta:
		ordering = ('id',)

class Ordersdetail(models.Model):
	quantity = models.IntegerField(verbose_name='cantidad')
	subtotal_amount = models.DecimalField(max_digits=6, decimal_places=2,verbose_name='subtotal');
	order = models.ForeignKey(Order,verbose_name='pedido')
	product = models.ForeignKey(Product,verbose_name='producto')

	def __str__(self):
		return '%s' % (self.product.name)

	class Meta:
		ordering = ('id',)
