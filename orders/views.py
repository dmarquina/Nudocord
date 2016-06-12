from django.shortcuts import render,redirect,get_object_or_404
from .models import Order, Ordersdetail
from clients.models import Client
from carts.models import Cart
from products.models import Product
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
			product=get_object_or_404(Product,pk=c.product.id)
			product.stock=product.stock-c.quantity
			product.save()
		Cart.objects.filter(client=client).delete()
		return redirect('/')
	else:	
		return redirect('/')

def orderlist(request):
	client = Client.objects.get(userprofile = request.user)
	context = getorderdata(client)
	context['cart_quantity'] = getcart(client)
	return render(request,'orders/order_list.html',context)

def orderdetail(request,pk):
	client = Client.objects.get(userprofile = request.user)
	order = get_object_or_404(Order, pk=pk)
	orderdetail=Ordersdetail.objects.filter(order=order)
	cantidad = 0
	for od in orderdetail:
		cantidad = cantidad + od.quantity
	context = {'order':order,
				'orderdetail':orderdetail,
				'cantidad':cantidad}
	context['cart_quantity'] = getcart(client)
	return render(request,'orders/order_list_detail.html',context)

def getorderdata(client):
	orders=Order.objects.filter(client=client)
	orderdata=[]
	for o in orders:
		orderdetail=Ordersdetail.objects.filter(order=o)
		aditionalprod=len(orderdetail)-1
		for od in orderdetail:
			firstprod=od.product
			break
		data={ 'id':o.id,
				'registration_date':o.registration_date,
				'amount':o.amount,
				'firstprod':firstprod,
				'aditionalprod':aditionalprod
			}
		orderdata.append(data)
	context = {'orderdata' : orderdata}
	return context

def getcart(client):
	cart = Cart.objects.filter(client=client)
	cart_quantity=0
	for c in cart:
		cart_quantity+=c.quantity
	return cart_quantity