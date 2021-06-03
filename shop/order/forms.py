from django import forms


class AddToOrderForm(forms.Form):
	product_id = forms.IntegerField(widget=forms.HiddenInput)
	count = forms.IntegerField(
		widget=forms.NumberInput(attrs={'class': 'form-control'}),
		label='تعداد'
	)
