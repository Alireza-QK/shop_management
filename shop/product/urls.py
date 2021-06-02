from django.urls import path
from .views import (
	ProductListHomeView,
	ProductListView,
	ProductDetailView,
	ProductCreateView,
	ProductUpdateView,
	GalleryListView,
	GalleryCreateView,
	GalleryUpdateView,
	GalleryDeleteView,
)

app_name = "product"

urlpatterns = [
	path('', ProductListHomeView.as_view(), name="home"),
	path('product_list/', ProductListView.as_view(), name="product_list"),
	path('product/<int:pk>/', ProductDetailView.as_view(), name="detail"),
	path('product_create/', ProductCreateView.as_view(), name="product_create"),
	path('product_update/<int:pk>', ProductUpdateView.as_view(), name="product_update"),
]

urlpatterns += [
	path('gallery_list/', GalleryListView.as_view(), name="gallery_list"),
	path('gallery_create/', GalleryCreateView.as_view(), name="gallery_create"),
	path('gallery_update/<int:pk>', GalleryUpdateView.as_view(), name="gallery_update"),
	path('gallery_delete/<int:pk>', GalleryDeleteView.as_view(), name="gallery_delete"),
]
