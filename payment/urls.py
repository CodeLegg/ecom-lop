from django.urls import path, include
from . import views

urlpatterns = [
    path("payment_success", views.payment_success, name="payment_success"),
    path('payment_failed', views.payment_failed, name='payment_failed'),
    path("checkout", views.checkout, name="checkout"),
    path("billing_info", views.billing_info, name="billing_info"),
    path("process_order", views.process_order, name="process_order"),
    path("my_orders", views.my_orders, name="my_orders"),
    path('orders/<int:pk>', views.orders, name='orders'),
    path('paypal/', include('paypal.standard.ipn.urls')),
]
