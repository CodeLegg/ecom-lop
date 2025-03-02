from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # Login & Logout URL
    path("login/", views.login_user, name="login"),
    path("register/", views.register_user, name="register"),
    path("update_user/", views.update_user, name="update_user"),
    path("update_info/", views.update_info, name="update_info"),
    path("update_password/", views.update_password, name="update_password"),
    path("logout/", views.logout_user, name="logout"),
    # Product
    path("product_list/", views.productlistAjax, name="product_list"),
    path("search_product/", views.search_product, name="search_product"),
    path("product/<int:pk>/", views.product, name="product"),
    path("category/<str:foo>/", views.category, name="category"),
    path(
        "category_children/<str:foo>/",
        views.category_children,
        name="category_children",
    ),
    path(
        "level_two_categories/<str:foo>/",
        views.level_two_categories,
        name="level_two_categories",
    ),
    path("all_categories/<str:foo>/", views.all_categories, name="all_categories"),
    # Bedroom Category
]
