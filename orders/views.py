from django.shortcuts import render,redirect
from .models import Order, Ordersdetail
from clients.models import Client
from carts.models import Cart
from deliverplaces.models import Deliverplace

def makeorder(request):
	if request.user.is_authenticated():
		pk_deliverplace = request.POST.get('deliverplacedate')
		client = Client.objects.get(userprofile = request.user)
		cart = Cart.objects.filter(client=client)
		deliverplace = Deliverplace.objects.get(pk=pk_deliverplace)
		amount = 0.0
		for c in cart:
			if amount == 0.0:
				amount = c.subtotal_amount
			else:
				amount = amount + c.subtotal_amount
		order = Order.objects.create(state='PR',
									client=client,
									amount=amount,
									deliverplace=deliverplace)
		for c in cart:
			Ordersdetail.objects.create(order=order,
										quantity=c.quantity,
										subtotal_amount=c.subtotal_amount,
										product=c.product)
		orders=Order.objects.filter(client=client)
		context = {'orders' : orders}
		return render(request,'orders/order_list.html',context)
	else:	
		return redirect('/')

def orderlist(request):
	client = Client.objects.get(userprofile = request.user)
	orders=Order.objects.filter(client=client)
	orderdata=[]
	for o in orders:
		orderdetail=Ordersdetail.objects.filter(order=o)
		aditionalprod=len(orderdetail)-1
		firstprod=orderdetail[0].product
		data={ 'id':o.id,
				'registration_date':o.registration_date,
				'amount':o.amount,
				'firstprod':firstprod,
				'aditionalprod':aditionalprod
			}
		orderdata.append(data)

	context = {'orderdata' : orderdata}

	return render(request,'orders/order_list.html',context)