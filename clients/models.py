from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
	name = models.CharField(max_length=255,verbose_name='nombre')
	lastname = models.CharField(max_length=255,verbose_name='apellido')
	phone = models.IntegerField(unique=True,verbose_name='teléfono')
	email = models.EmailField(max_length=255,verbose_name='email')
	address = models.CharField(max_length=255, verbose_name='dirección' )
	user = models.OneToOneField(User,default=True)

	def __str__(self):
		return self.name

	class Meta:
			ordering = ('id',)