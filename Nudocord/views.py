from django.shortcuts import render
from products.models import Product

def start(request):
	pk_products_cart = request.session.get('pk_products_cart',{})
	cart_quantity = request.session.get('cart_quantity',0)
	request.session['pk_products_cart'] = pk_products_cart
	request.session['cart_quantity'] = cart_quantity
	product_list = Product.objects.all()

	return render(request,'index.html',{
		'cart_quantity' : cart_quantity,
		'pk_products_cart': pk_products_cart,
		'product_list': product_list,
		})
