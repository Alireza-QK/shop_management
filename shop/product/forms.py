from django import forms
from .models import Product, GalleryProduct


class ProductForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'

	class Meta:
		model = Product
		fields = ('title', 'text', 'price', 'discount', 'image', 'stock_count')

	def clean_discount(self):
		price = self.cleaned_data.get('price')
		discount = self.cleaned_data.get('discount')

		if discount < price:
			return discount
		raise forms.ValidationError('Please discount is < price')


class GalleryProductForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'

	image = forms.FileField(
		widget=forms.ClearableFileInput(attrs={
			'multiple': True
		}),
		required=False
	)

	class Meta:
		model = GalleryProduct
		fields = ('product', 'image')
