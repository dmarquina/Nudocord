from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from .models import Product
from .mixins  import LoginRequiredMixin

class ProductDetail(LoginRequiredMixin, DetailView):
	model = Product
	
@method_decorator(login_required,name='dispatch')	
class ProductCreate(CreateView):
	model = Product
	fields = ['name','description','category','price','image','stock',]

