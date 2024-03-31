from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Bedroom Category
    path('beds/', views.beds, name='beds'),
    path('bedding/', views.bedding, name='bedding'),
    path('wardrobes/', views.wardrobes, name='wardrobes'),
    path('chestofdrawers/', views.chestofdrawers, name='chestofdrawers'),
    path('mattresses/', views.mattresses, name='mattresses'),
    path('bedsidetables/', views.bedsidetables, name='bedsidetables'),
    path('allbedroomfurniture/', views.allbedroomfurniture, name='allbedroomfurniture'),
]
