from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, TemplateView
from django.contrib.auth.decorators import login_required
from .models import Order, OrderDetail
from .forms import AddToOrderForm
from product.models import Product


@login_required
def add_to_cart(request):
	order_form = AddToOrderForm(request.POST or None, initial={'count': 1})

	if order_form.is_valid():
		order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
		if order is None:
			order = Order.objects.create(owner_id=request.user.id, is_paid=False)

		product_id = order_form.cleaned_data.get('product_id')
		count = order_form.cleaned_data.get('count')
		product = Product.objects.get(id=product_id)

		# Todo: Check product already added to order detail
		qs = OrderDetail.objects.filter(product_id=product.id)
		if qs.exists():
			for item in qs:
				item.count += count
				item.save()
		else:
			price_final = 0
			if product.discount > 0:
				price_final = product.discount
			else:
				price_final = product.price

			order.orderdetail_set.create(
				product_id=product.id,
				price=price_final,
				count=count
			)
		print(qs, qs.exists())
		# return qs

		return redirect(reverse('product:detail', kwargs={'pk': product_id}))


def cartView(request):
	context = {
		'order': None,
		'orderdetails': None
	}
	order: Order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()

	if order is not None:
		context['order'] = order
		context['orderdetails'] = order.orderdetail_set.all()

	return render(request, 'order/cart.html', context)

