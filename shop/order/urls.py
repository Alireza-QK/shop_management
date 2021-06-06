from django.urls import path
from .views import add_to_cart, updateCountItem, removItemCart, cartView

app_name = 'order'

urlpatterns = [
	path('add_to_cart/', add_to_cart, name="add_to_cart"),
	path('update_count_item/<int:product_id>/', updateCountItem, name="update_count_item"),
	path('remove_item_cart/<int:product_id>/', removItemCart, name="remove_item_cart"),
	path('cart/', cartView, name="cart"),
]