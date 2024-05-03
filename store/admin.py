from django.contrib import admin
from .models import Category, Customer, Product, Order, ProductImage, Color

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category_name', 'image_display')

    def parent_category_name(self, obj):
        if obj.parent_category:
            return obj.parent_category.name
        else:
            return '(No parent category)'
    parent_category_name.short_description = 'Parent Category'

    def image_display(self, obj):
        if obj.image:
            return '<img src="%s" width="100" />' % obj.image.url
        else:
            return '(No image)'
    image_display.allow_tags = True
    image_display.short_description = 'Image Preview'

admin.site.register(Category, CategoryAdmin)

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    filter_horizontal = ("colors",)

admin.site.register(Customer)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(Color)
