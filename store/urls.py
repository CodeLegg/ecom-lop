from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("allhomeandfurniture/", views.allhomeandfurniture, name="allhomeandfurniture"),
    # Login & Logout URL
    path("login/", views.login_user, name="login"),
    path("register/", views.register_user, name="register"),
    path("logout/", views.logout_user, name="logout"),
    # Product
    path('product/<int:pk>/', views.product, name='product'),
    # Bedroom Category
    path("beds/", views.beds, name="beds"),
    path("bedframes/", views.bedframes, name="bedframes"),
    path("bedding/", views.bedding, name="bedding"),
    path("wardrobes/", views.wardrobes, name="wardrobes"),
    path("chestofdrawers/", views.chestofdrawers, name="chestofdrawers"),
    path("mattresses/", views.mattresses, name="mattresses"),
    path("bedsidetables/", views.bedsidetables, name="bedsidetables"),
    path("allbedroomfurniture/", views.allbedroomfurniture, name="allbedroomfurniture"),
]
