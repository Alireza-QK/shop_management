from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.forms import inlineformset_factory, formset_factory, modelformset_factory
from django.views.generic import (
	ListView,
	CreateView,
	UpdateView,
	DeleteView,
	DetailView,
)
from .models import Product, GalleryProduct
from .forms import ProductForm, GalleryProductForm, GalleryUpdateProductForm


# ********************* Section for Product Model *********************
class ProductListView(ListView):
	model = Product
	template_name = 'product/product_list.html'


class ProductDetailView(DetailView):
	model = Product
	template_name = 'product/product_detail.html'


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
			messages.add_message(self.request, messages.SUCCESS, 'محصول شما با موفقیت ایجاد شد.')

		return render(self.request, self.template_name, context)


class ProductUpdateView(UpdateView):
	model = Product
	form_class = ProductForm
	template_name = 'product/product_create.html'
	success_url = reverse_lazy('product:home')


# ********************* Section for Gallery Model *********************
class GalleryListView(ListView):
	model = GalleryProduct
	template_name = 'gallery/gallery_list.html'


class GalleryCreateView(CreateView):
	model = GalleryProduct
	form_class = GalleryProductForm
	template_name = 'gallery/gallery_create.html'

	def post(self, request, *args, **kwargs):
		form_class = self.form_class
		form = self.get_form(form_class)
		context = {
			'form': form
		}

		if form.is_valid():
			product = form.cleaned_data.get('product')
			images = request.FILES.getlist('image')
			for image in images:
				GalleryProduct.objects.create(
					product=product,
					images=image
				)
			messages.add_message(request, messages.SUCCESS, 'گالری شما با موفقیت ایجاد شد.')
			print(product)
			print(images)

		return render(request, self.template_name, context)


class GalleryUpdateView(UpdateView):
	model = GalleryProduct
	form_class = GalleryUpdateProductForm
	template_name = 'gallery/gallery_update.html'
	success_url = reverse_lazy('product:home')


class GalleryDeleteView(DeleteView):
	model = GalleryProduct
	success_url = reverse_lazy('product:gallery_list')
	template_name = 'gallery/galleryproduct_confirm_delete.html'
