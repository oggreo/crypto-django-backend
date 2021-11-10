from django.contrib import admin
from .models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name', 'description']
    list_filter = ['description']

admin.site.register(Product, ProductAdmin)
