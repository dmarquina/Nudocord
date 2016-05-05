from django.contrib import admin
from .models import Order
from .models import Ordersdetail

@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
	list_display = ('client','amount')

@admin.register(Ordersdetail)
class AdminOrdersdetail(admin.ModelAdmin):
    list_display = ('product', 'quantity','subtotal_amount',)
