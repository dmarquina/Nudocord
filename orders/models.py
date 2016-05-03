from django.db import models
from clients.models import Client
from events.models import Event
from products.models import Product

class Order(models.Model):
	STATES_CHOICES = (
		('PR', 'Proceso'),
		('EN', 'Entregado'),
		('CA', 'Cancelado'),
	)
	state = models.CharField(max_length=2,verbose_name='estado',choices=STATES_CHOICES)
	total_price	= models.DecimalField(max_digits=6, decimal_places=2, verbose_name='precio total')
	registration_date = models.DateField(auto_now=False, auto_now_add=True, verbose_name='fecha',blank=True)	
	client = models.ForeignKey(Client, verbose_name='cliente')
	event = models.ForeignKey(Event,verbose_name='evento')

	def __str__(self):
		return '%s' % (self.client.name)

	class Meta:
		ordering = ('id',)



class Ordersdetail(models.Model):
	quantity = models.IntegerField(verbose_name='cantidad')
	subtotal_price = models.DecimalField(max_digits=6, decimal_places=2,verbose_name='subtotal');
	order = models.ForeignKey(Order,verbose_name='pedido')
	product = models.ForeignKey(Product,verbose_name='producto')

	def __str__(self):
		return '%s' % (self.product.name)

	class Meta:
		ordering = ('id',)
