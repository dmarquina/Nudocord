from django.db import models
from userprofiles.models import Userprofile

class ClientManager(models.Manager):
    def create_client(self, userprofile):
        client = self.create(userprofile=userprofile,)
        return client


class Client(models.Model):
	userprofile = models.OneToOneField(Userprofile, verbose_name='usuario')
	phone = models.IntegerField(verbose_name='teléfono',null=True)

	objects = ClientManager()

	def __str__(self):
		return '%s' % (self.userprofile.name)

	class Meta:
			ordering = ('id',)
