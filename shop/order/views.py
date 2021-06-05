from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, TemplateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.core.exceptions import ValidationError
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
			print(count)
			for item in qs:
				stock_count = item.product.stock_count
				if count > stock_count:
					raise ValidationError('تعداد خرید شما بزرگ تر از موجودی محصول می باشد. لطفا عدد درست وارد نمایید.')
				else:
					item.count += count
					item.product.stock_count -= count
					item.save()
					item.product.save()
		else:
			# this check discount and price
			price_final = 0
			if product.discount > 0:
				price_final = product.discount
			else:
				price_final = product.price
			
			# this check product stock count
			if count > product.stock_count:
				raise forms.ValidationError('تعداد خرید شما بزرگ تر از موجودی محصول می باشد. لطفا عدد درست وارد نمایید.')
			else:
				if count > 1:
					product.stock_count -= count
				else:
					product.stock_count -= 1
				product.save()

			order.orderdetail_set.create(
				product_id=product.id,
				price=price_final,
				count=count
			)
		print(qs, qs.exists())
		# return qs

		return redirect(reverse('product:detail', kwargs={'pk': product_id}))


def updateCountItem(request, product_id):
	order: Order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
	qs = OrderDetail.objects.filter(product_id=product_id)
	if qs.exists():
		count = request.POST.get('count')
		if int(count) < 0 or int(count) == 0:
			count = 1
		for item in qs:
			item.count = count
			item.save()

	order.orderdetail_set.all()
	return redirect(reverse('order:cart'))


def cartView(request):
	context = {
		'order': None,
		'orderdetails': None,
		'total': 0
	}
	order: Order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()

	if order is not None:
		context['order'] = order
		context['orderdetails'] = order.orderdetail_set.all()
		context['total'] = order.get_total_price_order()

	return render(request, 'order/cart.html', context)

