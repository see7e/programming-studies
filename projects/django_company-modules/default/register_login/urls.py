from django.urls import path
from . import views


app_name = "register_login"

urlpatterns = [
    path("", views.usr_login, name="login"),
    path("login/", views.usr_login, name="login"),
    path("logout/", views.usr_logout, name="logout"),
    path("register/", views.register, name="register"),
    path("home/", views.index, name="home"),
    path("profile/", views.usr_profile, name="profile"),
    path("profile/edit/", views.usr_profile_edit, name="profile_edit"),
]
