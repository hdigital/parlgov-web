from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

app_name = "page"

urlpatterns = [
    path("robots.txt", views.RobotsView.as_view(), name="robots"),
    path("login-parlgov", views.UserLoginView.as_view(), name="login"),
    path("logout-parlgov", LogoutView.as_view(), name="logout"),
    path("", views.home_view, name="home"),
]
