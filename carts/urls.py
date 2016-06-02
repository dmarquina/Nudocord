from django.conf.urls import url
from . import views
from .api import api_deliverplacesname
from .api import api_deliverplacesdate

urlpatterns = [
	url(r'^(?P<pk>[0-9]+)$', views.addtocart, name='addtocart'),
	url(r'^orders/cart_list/$', views.cartdetail, name='cartdetail'),
	url(r'^api/deliverplacesname/$', api_deliverplacesname, name='api_deliverplacesname'),
	url(r'^api/deliverplacesdate/(?P<pk>\d+)/$', api_deliverplacesdate, name='api_deliverplacesdate'),
]