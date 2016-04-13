from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$',views.ProductList.as_view(), name='hello'),
	url(r'^product/(?P<pk>[0-9]+)/$',views.ProductDetail.as_view(), name='detail'),
	url(r'^product/product_create$', views.ProductCreate.as_view(success_url="/"), name="create"),
]