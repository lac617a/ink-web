from django import template
from products.models import Category,Brands,Products

register = template.Library()

@register.simple_tag
def get_categories_aside():
  queryset = Category.objects.all()
  return queryset

@register.simple_tag
def get_brands_aside():
  queryset = Brands.objects.all()
  return queryset

@register.simple_tag
def get_count_brands_aside(brand):
  queryset = Products.objects.filter(pdBrand=Brands.objects.get(brName=brand))
  return queryset.count()

@register.simple_tag
def get_count_category_aside(category):
  queryset = Products.objects.filter(pdCategories=Category.objects.get(cgName=category))
  return queryset.count()