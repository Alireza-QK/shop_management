from django.urls import path
from .views import (
	ProductListView,
	ProductDetailView,
	ProductCreateView,
	ProductUpdateView,
	GalleryCreateView,
)

app_name = "product"

urlpatterns = [
	path('', ProductListView.as_view(), name="home"),
	path('product/<int:pk>/', ProductDetailView.as_view(), name="detail"),
	path('product_create/', ProductCreateView.as_view(), name="product_create"),
	path('product_update/<int:pk>', ProductUpdateView.as_view(), name="product_update"),
]

urlpatterns += [
	path('gallery_create/', GalleryCreateView.as_view(), name="gallery_create"),
	path('gallery_update/<int:pk>', GalleryCreateView.as_view(), name="gallery_update"),
]