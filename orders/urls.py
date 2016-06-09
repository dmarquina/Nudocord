from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^orders/makeorder/$', views.makeorder, name='makeorder'),
	url(r'^orders/order_list/$', views.orderlist, name='orderlist'),
]