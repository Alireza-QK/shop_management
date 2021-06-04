from django.urls import path
from .views import add_to_cart, updateCountItem, cartView

app_name = 'order'

urlpatterns = [
	path('add_to_cart/', add_to_cart, name="add_to_cart"),
	path('update_count_item/<int:product_id>/', updateCountItem, name="update_count_item"),
	path('cart/', cartView, name="cart"),
]