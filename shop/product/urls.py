from django.urls import path
from .views import (
	ProductListView,
	ProductCreateView,
	GalleryCreateView,
)

app_name = "product"

urlpatterns = [
	path('', ProductListView.as_view(), name="home"),
	path('product_create/', ProductCreateView.as_view(), name="product_create"),
]

urlpatterns += [
	path('gallery_create/', GalleryCreateView.as_view(), name="gallery_create"),
]