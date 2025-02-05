from django.contrib import admin
from .models import Product  # Changed from 'product' to 'Product'

# Register your models here.

class ProductAdmin(admin.ModelAdmin):  # Changed from 'productAdmin' to 'ProductAdmin'
    list_display = ('product_name', 'price', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}

admin.site.register(Product, ProductAdmin)  # Changed from 'product' to 'Product'
