from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterUserForm(UserCreationForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['username'].help_text = ''
		self.fields['password1'].help_text = ''
		self.fields['password2'].help_text = ''
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'
	
	phone_number = forms.RegexField(
		regex=r'(0|\+98)?([ ]|,|-|[()]){0,2}9[1|2|3|4]([ ]|,|-|[()]){0,2}(?:[0-9]([ ]|,|-|[()]){0,2}){8}',
		label='شماره موبایل',
		help_text='لطفا یک شماره موبایل درست و ایرانی وارد کنید',
		# widget=forms.NumberInput(attrs={'class': 'form-control'}),
		error_messages={
			'invalid': 'شماره موبایل معتبر نمی باشد.'
		}
	)

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'username', 'email', 'phone_number')
	
	def clean_phone_number(self):
		phone_number = self.cleaned_data.get('phone_number')
		
		if User.objects.filter(phone_number=phone_number).exists():
			raise forms.ValidationError('شما قبلا تر ثبت نام کردید لطفا وارد حساب شوید.')
		return phone_number

	def clean_email(self):
		email = self.cleaned_data.get('email')
		
		if User.objects.filter(email=email).exists():
			raise forms.ValidationError('شما قبلا تر ثبت نام کردید لطفا وارد حساب شوید.')
		return email


class LoginUserForm(forms.Form):

	username = forms.CharField(
		max_length=125,
		widget=forms.TextInput(attrs={'class': 'form-control'}),
		label='نام کاربری'
	)
	password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='کلمه عبور'
    )
	