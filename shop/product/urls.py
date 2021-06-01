from django.urls import path
from .views import (
	ProductListView,
	ProductCreateView,
)

app_name = "product"

urlpatterns = [
	path('', ProductListView.as_view(), name="home"),
	path('product_create', ProductCreateView.as_view(), name="product_create"),
]
