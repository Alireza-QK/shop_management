from django import forms


class AddToOrderForm(forms.Form):
	product_id = forms.IntegerField(widget=forms.HiddenInput)
	count = forms.IntegerField(
		widget=forms.NumberInput(attrs={'class': 'form-control'}),
		label='تعداد'
	)

	def clean_count(self):
		count = self.cleaned_data.get('count')

		if count < 0:
			count = 1

		return count
