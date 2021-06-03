from django.urls import path
from .views import AddToCartView

app_name = 'order'

urlpatterns = [
	path('add_to_cart/', AddToCartView.as_view(), name="add_to_cart"),
]