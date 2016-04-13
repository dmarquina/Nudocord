from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render,get_object_or_404

from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from .forms import ProductForm
from .models import Product

class ProductList(ListView):
	model = Product

class ProductDetail(DetailView):
	model = Product
			
class ProductCreate(CreateView):
	model = Product
	fields = ['name','description','category','price','image',]

#def new_product(request):
#	if request.method == 'POST':
#		#request.Files permite subir archivos, sin el solo es un POST cualquiera
#		form = ProductForm(request.POST,request.FILES)
#		if form.is_valid():
#			product = form.save()
#			product.save()
#			return HttpResponseRedirect('/')
#	else:
	#	form = ProductForm()
#
#	template = loader.get_template('new_product.html')
#	context = {
#		'form' : form
#	}	
#	return HttpResponse(template.render(context, request))

