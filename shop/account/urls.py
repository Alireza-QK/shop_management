from django.urls import path
from .views import UserRegisterView, UserLoginView, logoutUser, activate

app_name = 'account'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('logout/', logoutUser, name="logout"),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
]
