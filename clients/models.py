#from django.db import models
#from django.contrib.auth.models import User

#class Client(models.Model):
#	name = models.CharField(max_length=255,verbose_name='nombre')
#	lastname = models.CharField(max_length=255,verbose_name='apellido')
#	phone = models.IntegerField(unique=True,verbose_name='teléfono')
#	email = models.EmailField(max_length=255,verbose_name='email')
#	user = models.OneToOneField(User,default=True)
#
#	def __str__(self):
#		return self.name
#
#	class Meta:
#			ordering = ('id',)

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class ClientManager(BaseUserManager):
    def create_user(self, email, name,lastname, password=None):
        """
        Creates and saves a User with the given email,name 
        and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            lastname=lastname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name,lastname, password):
        """
        Creates and saves a superuser with the given email, name
        and password.
        """
        user = self.create_user(email,
            password=password,
            name=name,
            lastname=lastname,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Client(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    celphone = models.IntegerField(null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = ClientManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','lastname']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin