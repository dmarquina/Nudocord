from django.shortcuts import render
from .models import Order, Orderdetail
from clients.models import Client

def makeorder(request):
	if request.user.is_authenticated():
		client = Client.objects.get(userprofile = request.user)
		cart = Cart.objects.filter(client=client)
		for c in cart:
			amount+= c.subtotal_amount
		order = Order.objects.create(state='PR',
									client=client,
									amount=amount,
									deliverplace=)
		for c in cart:
			Orderdetail.objects.create(order=order,
										quantity=c.quantity,
										subtotal_amount=c.subtotal_amount,
										product=c.product)
	else:	