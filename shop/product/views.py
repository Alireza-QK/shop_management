from django.shortcuts import render
from django.views.generic import (
	ListView,
	CreateView,
)
from .models import Product, GalleryProduct
from .forms import ProductForm, GalleryProductForm


class ProductListView(ListView):
	model = Product
	template_name = 'product/product_list.html'

# Show detail product


class ProductCreateView(CreateView):
	model = Product
	form_class = ProductForm
	template_name = 'product/product_create.html'
