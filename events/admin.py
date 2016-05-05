from django.contrib import admin
from .models import Event

@admin.register(Event)
class AdminEvent(admin.ModelAdmin):
	list_display = ('name','address','date',)
	list_filter = ('name',)