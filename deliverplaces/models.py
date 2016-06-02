from django.db import models

class Deliverplace(models.Model):
	name = models.CharField(max_length=140,verbose_name='nombre')
	address = models.CharField(max_length=255,verbose_name='direccion')
	date = models.DateTimeField(auto_now=False, auto_now_add=False,null=True, verbose_name='fecha')	

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('id',)
		unique_together = ('name', 'address','date')