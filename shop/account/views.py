from django.shortcuts import render
from django.views.generic import CreateView, FormView
from django.contrib.auth.views import LoginView
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from .models import User
from .forms import RegisterUserForm
from .utils import account_activation_token


class UserRegisterView(CreateView):
	model = User
	template_name = 'account/auth/register.html'
	form_class = RegisterUserForm

	def form_valid(self, form):
		response = form.save(commit=False)
		context = {'form': None}

		if form.is_valid():
			first_name = form.cleaned_data.get('first_name')
			last_name = form.cleaned_data.get('last_name')
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			phone_number = form.cleaned_data.get('phone_number')
			response.is_active = False
			form.save()
			current_site = get_current_site(self.request)
			mail_subject = 'تایئد حساب کاربری'
			message = render_to_string('account/auth/account_activaction.html', {
				'user': response,
				'domain': current_site.domain,
				'uid': urlsafe_base64_encode(force_bytes(response.pk)),
				'token': account_activation_token.make_token(response),
			})
			to_email = form.cleaned_data.get('email')
			email = EmailMessage(
				mail_subject, message, to=[to_email]
			)
			email.send()
			return HttpResponse('Please confirm your email address to complete the registration')
		else:
			form = form
		
		context = {
			'form': form
		}
		
		return render(self.request, self.template_name, context)


def activate(request, uidb64, token):
	try:
		uid = urlsafe_base64_decode(uidb64).decode()
		user = User.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
	else:
		return HttpResponse('Activation link is invalid!')
