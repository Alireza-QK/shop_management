from django.urls import path
from .views import UserRegisterView, UserLoginView, activate

app_name = 'account'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
]
