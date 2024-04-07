from django.shortcuts import render
from .models import Product

# Create your views here.
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

def filter_products(request):
    # Retrieve all distinct price values
    price_ranges = Product.objects.values_list('price', flat=True).distinct().order_by('price')

    # Handle filtering
    if 'price_filter' in request.GET:
        selected_price = request.GET.get('price_filter')
        if selected_price:
            # Filter products based on selected price
            products = Product.objects.filter(price=selected_price)
        else:
            # If no price selected, show all products
            products = Product.objects.all()
    else:
        products = Product.objects.all()

    return render(request, 'filter_products.html', {'products': products, 'price_ranges': price_ranges})