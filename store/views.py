from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, RegistrationForm
from django.contrib.auth.models import User


def home(request):
    return render(request, "home.html", {})  # render the home.html template


def allhomeandfurniture(request):
    return render(
        request, "allhomeandfurniture.html", {}
    )  # render the home.html template


def beds(request):
    return render(request, "beds.html", {})  # render the home.html template


def bedframes(request):
    products = Product.objects.all()
    return render(
        request, "bedframes.html", {"products": products}
    )  # render the home.html template


def bedding(request):
    return render(request, "bedding.html", {})  # render the home.html template


def wardrobes(request):
    return render(request, "wardrobes.html", {})  # render the home.html template


def chestofdrawers(request):
    return render(request, "chestofdrawers.html", {})  # render the home.html template


def mattresses(request):
    return render(request, "mattresses.html", {})  # render the home.html template


def bedsidetables(request):
    return render(request, "bedsidetables.html", {})  # render the home.html template


def allbedroomfurniture(request):
    return render(
        request, "allbedroomfurniture.html", {}
    )  # render the home.html template


def login_or_register(request):
    if request.method == "POST":
        if "login" in request.POST:
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data["username"]
                password = login_form.cleaned_data["password"]
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "You have successfully logged in.")
                    return redirect("home")
                else:
                    messages.warning(request, "Invalid username or password.")
                    return redirect("login_or_register")
        elif "register" in request.POST:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                username = registration_form.cleaned_data["username"]
                if User.objects.filter(username=username).exists():
                    messages.warning(request, "Username is already taken.")
                    return redirect("login_or_register/#")
                password1 = registration_form.cleaned_data["password1"]
                password2 = registration_form.cleaned_data["password2"]
                if password1 != password2:
                    messages.warning(request, "Passwords do not match.")
                    return redirect("login_or_register/#")
                else:
                    user = User.objects.create_user(username=username, password=password1)
                    login(request, user)
                    messages.success(request, "You have successfully registered and logged in.")
                    return redirect("home")
    else:
        login_form = LoginForm()
        registration_form = RegistrationForm()

    context = {"login_form": login_form, "registration_form": registration_form}
    return render(request, "login_or_register.html", context)

def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect("home")
