from django.urls import path
from .views import add_to_cart, cartView

app_name = 'order'

urlpatterns = [
	path('add_to_cart/', add_to_cart, name="add_to_cart"),
	path('cart/', cartView, name="cart"),
]