from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from products.models import Product

def addtocart(request,pk):
	cart_quantity = request.session.get('cart_quantity')
	pk_products_cart = request.session.get('pk_products_cart')
	if str(pk) in pk_products_cart:
		pk_products_cart[str(pk)]+=1
	else:
		pk_products_cart[str(pk)]=1
	cart_quantity+=1	
	request.session['pk_products_cart'] = pk_products_cart
	request.session['cart_quantity'] = cart_quantity
	return redirect('/')

def cartdetail(request):
	cart_quantity = request.session.get('cart_quantity')
	pk_products_cart = request.session.get('pk_products_cart')
	products_cart=[]
	for pk_product in pk_products_cart:
		products_cart.append(get_object_or_404(Product, pk=int(pk_product)))
	return render(request, 'orders/cart_list.html',{
		'products_cart': products_cart,
		'cart_quantity': cart_quantity,
		})