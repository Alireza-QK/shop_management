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

	def form_valid(self, form):
		response = form.save(commit=False)
		context = {
			'form': form
		}
		if form.is_valid():
			title = form.cleaned_data.get('title')
			text = form.cleaned_data.get('text')
			image = form.cleaned_data.get('image')
			price = form.cleaned_data.get('price')
			discount = form.cleaned_data.get('discount')
			stock_count = form.cleaned_data.get('stock_count')

			Product.objects.create(
				title=title,
				text=text,
				image=image,
				price=price,
				discount=discount,
				stock_count=stock_count
			)

		return render(self.request, self.template_name, context)
