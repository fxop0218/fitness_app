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
    path("create-exercise/", views.create_exercise, name="create_exercise"),
    path(
        "create-training-session/",
        views.create_training_session,
        name="create_training_session",
    ),
]
