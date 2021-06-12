from django.urls import path
from .views import windowMain, termsAndConditions,productsViews

app_name="Main"

urlpatterns = [
  path('',windowMain, name='windowMain'),
  path('termsAndCondition/',termsAndConditions,name='terms'),
  path('products/',productsViews,name='pro')
]