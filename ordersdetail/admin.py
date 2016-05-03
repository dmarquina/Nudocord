from django.contrib import admin
from .models import Ordersdetail

@admin.register(Ordersdetail)
class AdminOrdersdetail(admin.ModelAdmin):
	list_display = ('product','quantity')

