from django.contrib import admin
from .models import Deliverplace

@admin.register(Deliverplace)
class AdminDeliverplace(admin.ModelAdmin):
	list_display = ('name','address','date',)
	list_filter = ('name',)