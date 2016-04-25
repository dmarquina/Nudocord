from django.db import models
from clients.models import Client

class Product(models.Model):
	name = models.CharField(max_length=255, verbose_name='nombre')
	description = models.CharField(max_length=255,verbose_name='descripción')
	category = models.CharField(max_length=255, verbose_name='categoria')
	price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='precio')
	image = models.ImageField(blank=True, verbose_name='imagen')
	
	def __str__(self):
		return self.name

	class Meta:
		ordering = ('id',)

class Favorite(models.Model):
	user = models.ForeignKey(Client)
	product = models.ForeignKey(Product)

	class Meta:
		verbose_name = 'Favorito'
		verbose_name_plural = 'Favoritos'

	def __str__(self):
			return '%s %s' % (self.user.name, self.product.name)