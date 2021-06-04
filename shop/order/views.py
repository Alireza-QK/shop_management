from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, TemplateView
from .models import Order, OrderDetail
from .forms import AddToOrderForm
from product.models import Product


def add_to_cart(request):
	order_form = AddToOrderForm(request.POST or None, initial={'count': 1})

	if order_form.is_valid():
		order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
		if order is None:
			order = Order.objects.create(owner_id=request.user.id, is_paid=False)

		product_id = order_form.cleaned_data.get('product_id')
		print(product_id)

		count = order_form.cleaned_data.get('count')
		product = Product.objects.get(id=product_id)
		print(product)

		order.orderdetail_set.create(
			product_id=product.id,
			price=product.price,
			count=count
		)

		return redirect(reverse('product:detail', kwargs={'pk': product_id}))
