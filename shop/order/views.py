from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from .models import Order, OrderDetail
from .forms import AddToOrderForm


class AddToCartView(FormView):
	form_class = AddToOrderForm
	template_name = 'order/add_to_cart.html'
