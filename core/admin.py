from django.contrib import admin
from .models import Brands, Products,Category

# Register your models here.

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
  pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  pass

@admin.register(Brands)
class BrandsAdmin(admin.ModelAdmin):
  pass
