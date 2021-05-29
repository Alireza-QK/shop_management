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

