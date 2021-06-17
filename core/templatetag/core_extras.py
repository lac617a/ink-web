from django import template
from products.models import Category

register = template.Library()

@register.simple_tag
def get_categories_aside():
  queryset = Category.objects.all()
  return queryset