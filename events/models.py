from django.db import models

class Event(models.Model):
	name = models.CharField(max_length=140,verbose_name='nombre')
	address = models.CharField(max_length=255,verbose_name='direccion')
	date = models.DateField(auto_now=False, auto_now_add=False, verbose_name='fecha')	

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('id',)