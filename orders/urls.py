from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^orders/order_list/(?P<pk>\d+)/$', views.makeorder, name='makeorder'),
]