from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from accounts.views import signup


urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path("signup/", signup, name="signup"),
]
