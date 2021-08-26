from django.urls import path

from . import views

app_name="home"
urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.dashboard, name="home"),
    path("login/", views.loginPage, name="login"),
    path("register/", views.registerPage, name="register"),
    path("logout/", views.logoutPage, name="logout"),
]