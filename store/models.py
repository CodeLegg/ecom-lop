from django.db import models
import datetime
from django.utils import timezone



class Category(models.Model):
    CATEGORY_TYPE_CHOICES = [
        ('type', 'By Type'),
        ('size', 'By Size'),
    ]
    
    name = models.CharField(max_length=50)
    parent_category = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='subcategories',
        null=True,
        blank=True
    )
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)
    category_type = models.CharField(max_length=10, choices=CATEGORY_TYPE_CHOICES, default='type')

    def __str__(self):
        return self.name



# Customers
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Color(models.Model):
    name = models.CharField(max_length=100)
    hex_code = models.CharField(max_length=7, blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    about_this_product = models.TextField(blank=True, null=True)
    what_type = models.CharField(max_length=100, blank=True, null=True)
    material = models.CharField(max_length=100, blank=True, null=True)
    colors = models.ManyToManyField(
        Color, blank=True
    )  # Many-to-many relationship with Color
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )

    # Dimensions
    dimension_a = models.CharField(max_length=20, blank=True, null=True)
    dimension_b = models.CharField(max_length=20, blank=True, null=True)
    dimension_c = models.CharField(max_length=20, blank=True, null=True)
    dimension_d = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="reviews"
    )
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    text = models.TextField()
    star_rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = (
            "product",
            "user",
        )  # Ensure each user can only review a product once

    def __str__(self):
        return f"{self.user} - {self.product} - {self.date_posted}"


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="uploads/product/")

    def __str__(self):
        return f"Image for {self.product.name}"


# Orders
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default="", blank=True, null=True)
    phone = models.CharField(max_length=20, default="", blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.product
        # return f'{self.product.name} {self.customer.first_name} {self.customer.last_name}'
