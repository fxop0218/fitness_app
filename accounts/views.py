from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django import forms
from .models import CustomUser, WeightEntry
from django.contrib.auth.decorators import login_required
from .forms import WeightEntryForm, ExerciseForm

import datetime


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label="Repeat password")

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password", "password2", "date_of_birth"]

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Passwords don't match.")
        return cd["password2"]

    def clean_date_of_birth(self):
        cd = self.cleaned_data
        if cd["date_of_birth"] > datetime.date.today():
            raise forms.ValidationError("Invalid date of birth.")
        return cd["date_of_birth"]


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data["password"])
            new_user.save()
            return redirect("registration_success")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})


def registration_success(request):
    return render(request, "accounts/registration_success.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("landing_page")


@login_required
def add_weight(request):
    if request.method == "POST":
        form = WeightEntryForm(request.POST)
        if form.is_valid():
            weight_entry = form.save(commit=False)
            weight_entry.user = request.user
            weight_entry.save()
            return redirect("dashboard")
    else:
        form = WeightEntryForm()
    return render(request, "accounts/add_weight.html", {"form": form})


@login_required
def dashboard(request):
    weight_entries = WeightEntry.objects.filter(user=request.user).order_by("date")
    print(f"Peso: {weight_entries}")  # Agrega esta línea
    return render(request, "dashboard.html", {"weight_entries": weight_entries})


@login_required
def create_exercise(request):
    form = ExerciseForm(request.POST, request.FILES)
    if form.is_valid():
        exercise = form.save(commit=False)
        exercise.user = request.user
        exercise.save()
        form.save_m2m()  # Save many to many relations
        return redirect("dashboard")
    else:
        form = ExerciseForm()
    return render(request, "accounts/create_exercise.html", {"form": form})


@login_required
def create_training_session(request):
    return render(request, "accounts/create_training_session.html")


# Create your views here.
