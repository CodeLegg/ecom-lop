from django.shortcuts import render
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect


def home (request):
  return render(request, 'home.html', {}) # render the home.html template

def allhomeandfurniture (request):
  return render(request, 'allhomeandfurniture.html', {}) # render the home.html template


def beds (request):
  return render(request, 'beds.html', {}) # render the home.html template

def bedframes (request):
  products = Product.objects.all()
  return render(request, 'bedframes.html', {'products':products}) # render the home.html template

def bedding (request):
  return render(request, 'bedding.html', {}) # render the home.html template

def wardrobes (request):
  return render(request, 'wardrobes.html', {}) # render the home.html template

def chestofdrawers (request):
  return render(request, 'chestofdrawers.html', {}) # render the home.html template

def mattresses (request):
  return render(request, 'mattresses.html', {}) # render the home.html template

def bedsidetables (request):
  return render(request, 'bedsidetables.html', {}) # render the home.html template

def allbedroomfurniture (request):
  return render(request, 'allbedroomfurniture.html', {}) # render the home.html template

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect('home')
        else:
            messages.warning(request, "Unsuccessful. Please try again.")
            return redirect('login')
    else:
        return render(request, 'login.html', {})



def logout_user(request):
  logout(request)
  messages.success(request, "You have successfully logged out.")
  return redirect('home')

