from django.shortcuts import render, get_object_or_404
from products.models import Product
from clients.models import Client
from carts.models import Cart

def start(request):
	pk_products_cart = request.session.get('pk_products_cart',{})
	if request.user.is_authenticated():
		client = Client.objects.get(userprofile=request.user)
		if pk_products_cart != {}:
			for pk_product , quantity in pk_products_cart.items():
				product = get_object_or_404(Product, pk=int(pk_product))
				subtotal_amount = product.price * quantity
				try:
					cart = Cart.objects.get(product=product,
											client=client,)
					cart.quantity+=quantity
					cart.subtotal_amount+=subtotal_amount
					cart.save()
				except Cart.DoesNotExist:
					Cart.objects.create(product=product,
										client=client,
										quantity=quantity,
										subtotal_amount=subtotal_amount,)
			pk_products_cart.clear()
			request.session['pk_products_cart'] = pk_products_cart
		cart_quantity=0		
		for quantity in Cart.objects.values_list('quantity',flat=True).filter(client=client):
			cart_quantity+=quantity
	else:
		cart_quantity = request.session.get('cart_quantity',0)
		request.session['pk_products_cart'] = pk_products_cart
		request.session['cart_quantity'] = cart_quantity

	product_list = Product.objects.all()

	return render(request,'index.html',{
		'cart_quantity' : cart_quantity,
		'pk_products_cart': pk_products_cart,
		'product_list': product_list,
		})
