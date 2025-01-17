from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def landing_page(request):
    return render(request, "landing.html")


@login_required
def home(request):
    return render(request, "home.html")


@login_required
def dashboard(request):
    return render(request, "dashboard.html")
