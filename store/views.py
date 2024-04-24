from django.shortcuts import render, get_object_or_404
from .models import Product, Review
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .forms import LoginForm, RegistrationForm
from django.http import HttpResponseRedirect
from .forms import ReviewForm, EditReviewForm, DeleteReviewForm  # Import your ReviewForm
from django.db.models import Avg
from django.contrib.auth.decorators import login_required



@login_required
def product(request, pk):
    # Retrieve the product object or return a 404 error if not found
    product = get_object_or_404(Product, pk=pk)
    
    # Retrieve all reviews related to the product
    reviews = product.reviews.all()

    # Calculate average star rating for the product
    average_rating = reviews.aggregate(Avg('star_rating'))['star_rating__avg']

    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        # Check if editing a review
        if 'edit_review' in request.POST:
            review_to_edit = get_object_or_404(Review, pk=request.POST.get('edit_review'))
            edit_form = EditReviewForm(request.POST, instance=review_to_edit)
            if edit_form.is_valid():
                edit_form.save()
                return HttpResponseRedirect(request.path_info)
        # Check if deleting a review
        elif 'delete_review' in request.POST:
            delete_form = DeleteReviewForm(request.POST)
            if delete_form.is_valid() and delete_form.cleaned_data['confirm_delete']:
                review_to_delete = get_object_or_404(Review, pk=request.POST.get('delete_review'))
                review_to_delete.delete()
                return HttpResponseRedirect(request.path_info)
        # Otherwise, it's a new review submission
        else:
            form = ReviewForm(request.POST)
            if form.is_valid():
                new_review = form.save(commit=False)
                new_review.product = product
                new_review.user = request.user  # Assuming you have user authentication
                new_review.save()
                return HttpResponseRedirect(request.path_info)

    else:
        form = ReviewForm()
        edit_form = EditReviewForm()
        delete_form = DeleteReviewForm()

    # Create a list containing numbers 1 to 5 for star ratings
    stars_range = range(1, 6)

    # Check if the user has already submitted a review for this product
    user_has_review = reviews.filter(user=request.user).exists()

    # Render the product.html template with the necessary context data
    return render(request, 'product.html', {
        'product': product,
        'reviews': reviews,
        'form': form,
        'average_rating': average_rating,
        'stars_range': stars_range,
        'edit_form': edit_form,
        'delete_form': delete_form,
        'user_has_review': user_has_review,
    })



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
            # Check if the username exists in a case-insensitive manner
            user = User.objects.filter(username__iexact=username).first()
            if user is not None and user.check_password(password):
                login(request, user)
                messages.success(request, "You have successfully logged in.")
                next_url = request.POST.get("next")
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect("home")
            else:
                messages.warning(request, "Unsuccessful login. Please try again.")
    else:
        login_form = LoginForm()
        next_url = request.GET.get("next")
        if next_url:
            # If next_url exists in GET parameters, it's a redirection from a page
            return render(request, "login.html", {"login_form": login_form, "next": next_url})
        else:
            # If next_url doesn't exist, it's a direct login attempt
            return render(request, "login.html", {"login_form": login_form})

    # If the code reaches here, it means a 404 error occurred
    # Redirect the user to the login page with a warning message
    messages.warning(request, "Something Went Wrong. Please Try Again!")
    return redirect("login")

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
                next_url = request.POST.get("next")  # Get next_url from POST data
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect("home")
            else:
                # Something went wrong with authentication
                messages.warning(request, "Failed to sign you in. Please try again.")
        else:
            # Handle invalid registration form submission
            next_url = request.POST.get("next")  # Get next_url from POST data
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
        next_url = request.GET.get("next")
    
    # Pass registration_form and next_url to the template
    return render(
        request, "register.html", {"registration_form": registration_form, "next": next_url}
    )


def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect("home")
