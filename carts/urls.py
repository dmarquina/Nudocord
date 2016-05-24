from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^/(?P<pk>[0-9]+)$', views.addtocart, name='addtocart'),
	url(r'^orders/cart_list/$', views.cartdetail, name='cartdetail'),
]