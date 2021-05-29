from django.shortcuts import render
from django.views.generic import CreateView, FormView
from django.contrib.auth.views import LoginView
from .models import User
from .forms import RegisterUserForm


class UserRegisterView(CreateView):
    model = User
    template_name = 'account/auth/register.html'
    form_class = RegisterUserForm

