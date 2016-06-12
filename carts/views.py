from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from products.models import Product
from .models import Cart
from clients.models import Client
from deliverplaces.models import Deliverplace

def addtocart(request,pk):
	if request.user.is_authenticated():
		product = get_object_or_404(Product, pk=pk)
		client = Client.objects.get(userprofile=request.user)
		if Cart.objects.filter(product=product,client=client).exists():
			cart = Cart.objects.get(product=product,client=client)
			cart.quantity+=1
			cart.subtotal_amount+=product.price
			cart.save()
		else:
			Cart.objects.create(quantity=1,
								subtotal_amount=product.price,
								product=product,
								client=client)
	else:	
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
	cart=[]
	phone=0
	if request.user.is_authenticated():
		client = Client.objects.get(userprofile=request.user)
		phone = client.phone
		cart = Cart.objects.filter(client=client)
		cart_quantity=0
		for c in cart:
			cart_quantity+=c.quantity
	else:	
		cart_quantity = request.session.get('cart_quantity')
		pk_products_cart = request.session.get('pk_products_cart')
		for pk_product , quantity in pk_products_cart.items():
			product = get_object_or_404(Product, pk=int(pk_product))
			subtotal_amount = product.price * quantity
			cart.append(Cart(quantity=quantity,
							subtotal_amount=subtotal_amount,
							product=product))
	return render(request, 'orders/cart_list.html',{
		'cart': cart,
		'cart_quantity': cart_quantity,
		'phone': phone,		
		}
		)