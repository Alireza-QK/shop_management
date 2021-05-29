from django import forms
from .models import User

class RegisterUserForm(forms.ModelForm):

    def __init__(self):
        pass

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        