from django.contrib import admin
from .models import Order

@admin.register(Order)
class AdminProduct(admin.ModelAdmin):
	list_display = ('client','total_price')
