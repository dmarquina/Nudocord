from django.db import models

class Client(models.Model):
	name = models.CharField(max_length=255,verbose_name='nombre')
	phone = models.IntegerField(unique=True,verbose_name='teléfono')
	email = models.EmailField(max_length=255,verbose_name='email')
	address = models.CharField(max_length=255, verbose_name='dirección' )

	def __str__(self):
		return self.name

	class Meta:
			ordering = ('id',)