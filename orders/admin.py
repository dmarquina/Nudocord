from django.contrib import admin
from .models import Order

@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
	list_display = ('client','total_price')
