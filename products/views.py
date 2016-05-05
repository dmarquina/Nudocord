from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import (
    get_object_or_404, 
    redirect
)

from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from .models import Product
from .mixins  import LoginRequiredMixin

class ProductList(ListView):
	model = Product

class ProductDetail(LoginRequiredMixin, DetailView):
	model = Product
	
@method_decorator(login_required,name='dispatch')	
class ProductCreate(CreateView):
	model = Product
	fields = ['name','description','category','price','image',]