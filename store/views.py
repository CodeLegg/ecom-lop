from django.shortcuts import render

# Create your views here.
def home (request):
  return render(request, 'home.html', {}) # render the home.html template

def allhomeandfurniture (request):
  return render(request, 'allhomeandfurniture.html', {}) # render the home.html template


def beds (request):
  return render(request, 'beds.html', {}) # render the home.html template

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