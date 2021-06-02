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
		raise forms.ValidationError('قیمت با تخفیف باید از قیمت اصلی محصول کوچک تر باشد.')

	def clean_price(self):
		price = self.cleaned_data.get('price')
		if price < 0 or price == 0:
			raise forms.ValidationError('لطفا یک قیمت درست وارد کنید.')

		return price

	def clean_stock_count(self):
		stock_count = self.cleaned_data.get('stock_count')
		if stock_count == 0 or stock_count < 0:
			raise forms.ValidationError('لطفا تعداد موجودی درست وارد نمایید.')

		return stock_count


class GalleryProductForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'

	image = forms.FileField(
		widget=forms.ClearableFileInput(attrs={
			'multiple': True
		}),
		required=True
	)

	class Meta:
		model = GalleryProduct
		fields = ('product', 'image')


class GalleryUpdateProductForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'

	class Meta:
		model = GalleryProduct
		fields = ('product', 'images')
