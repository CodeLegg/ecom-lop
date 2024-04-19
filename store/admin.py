from django.contrib import admin
from .models import Category, Customer, Product, Order, ProductImage
from .models import Color


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    filter_horizontal = ("colors",)  # Allows selecting multiple colors easily


admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product, ProductAdmin)  # Register Product with custom admin options
admin.site.register(Order)
admin.site.register(Color)
