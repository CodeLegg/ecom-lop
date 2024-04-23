from django.shortcuts import render, get_object_or_404
from .models import Product, Review
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .forms import LoginForm, RegistrationForm
from django.http import HttpResponseRedirect
from .forms import ReviewForm  # Import your ReviewForm
from django.db.models import Avg

def product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = product.reviews.all()

    # Calculate average star rating
    average_rating = reviews.aggregate(Avg('star_rating'))['star_rating__avg']

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.product = product
            new_review.user = request.user  # Assuming you have user authentication
            new_review.save()
            return HttpResponseRedirect(request.path_info)  # Redirect to the same page after submission
    else:
        form = ReviewForm()

    # Create a list containing numbers 1 to 5
    stars_range = range(1, 6)

    return render(request, 'product.html', {'product': product, 'reviews': reviews, 'form': form, 'average_rating': average_rating, 'stars_range': stars_range})



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


def login_user(request):
    if request.method == "POST":
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
    else:
        login_form = LoginForm()

    return render(request, "login.html", {"login_form": login_form})


def register_user(request):
    if request.method == "POST":
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            username = registration_form.cleaned_data["username"]
            email = registration_form.cleaned_data["email"]
            password = registration_form.cleaned_data["password1"]
            # Create user object
            user = User.objects.create_user(
                username=username, email=email, password=password
            )
            # Authenticate user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Log the user in
                login(request, user)
                messages.success(
                    request, "You've successfully signed-up and signed-in."
                )
                return redirect("home")
            else:
                # Something went wrong with authentication
                messages.warning(request, "Failed to sign you in. Please try again.")
        else:
            # Handle invalid registration form submission
            if "username" in registration_form.errors:
                messages.warning(request, "This username is already taken.")
            elif "email" in registration_form.errors:
                messages.warning(
                    request, "This email is already associated with another account."
                )
            elif "password2" in registration_form.errors:
                messages.warning(request, "The passwords do not match.")
            else:
                messages.warning(request, "Registration failed. Please try again.")
    else:
        registration_form = RegistrationForm()

    return render(request, "register.html", {"registration_form": registration_form})


def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect("home")
