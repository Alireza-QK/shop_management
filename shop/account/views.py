from django.shortcuts import render
from django.views.generic import CreateView, FormView
from django.contrib.auth.views import LoginView
from .models import User


class UserRegisterView(LoginView):
    model = User
    template_name = 'account/auth/register.html'
    # form_class = User
    fields = ('username', 'email', 'phone_number')
