from django.shortcuts import render
from django.views.generic import FormView
from .models import User


class LoginView(FormView):
    model = User
    fields = ('username', 'frist_name', 'last_name', 'email', 'phone_number')
    template_name = 'account/auth/register.html'

