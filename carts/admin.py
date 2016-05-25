from django.contrib import admin
from .models import Cart

@admin.register(Cart)
class AdminCart(admin.ModelAdmin):
	list_display = ('product','quantity','subtotal_amount','client')