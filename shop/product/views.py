from django.shortcuts import render
from django.views.generic import ListView
from .models import Product, GalleryProduct


class ProductListView(ListView):
	model = Product
	template_name = 'product/product_list.html'
