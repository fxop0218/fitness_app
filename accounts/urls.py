from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path(
        "registration-success/", views.registration_success, name="registration_success"
    ),
    path("add-weight/", views.add_weight, name="add_weight"),
    path("dashboard/", views.dashboard, name="dashboard"),
]
