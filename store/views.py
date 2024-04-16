from django.shortcuts import render
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .forms import LoginForm, RegistrationForm


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
    login_form = LoginForm()
    registration_form = RegistrationForm()

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
                    messages.warning(request, "Unsuccessful login. Please try again.")
        elif "register" in request.POST:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                username = registration_form.cleaned_data["username"]
                email = registration_form.cleaned_data["email"]
                password = registration_form.cleaned_data["password1"]
                User.objects.create_user(
                    username=username, email=email, password=password
                )
                messages.success(
                    request, "You've successfully signed-up and signed-in."
                )
                return redirect("home")
            # Handling form errors
            # If the registration form is not valid, it means there are validation errors
            else:
                # If the error is due to duplicate username
                if "username" in registration_form.errors:
                    messages.warning(request, "This username is already taken.")
                elif "email" in registration_form.errors:
                    messages.warning(request, "This email is already associated with an existing account.")
                # If the error is due to password mismatch
                elif "password2" in registration_form.errors:
                    messages.warning(request, "The passwords do not match.")
                else:
                    messages.warning(request, "Registration failed. Please try again.")

    context = {"login_form": login_form, "registration_form": registration_form}
    return render(request, "login_or_register.html", context)


def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect("home")
