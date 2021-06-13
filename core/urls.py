from django.urls import path
from .views import (windowMain, termsAndConditions,productsViews,productDelete,productEdit,productsHidden)

app_name="Main"

urlpatterns = [
  path('',windowMain, name='windowMain'),
  path('products/',productsViews,name='pro'),
  path('product/edit/<int:id>/',productEdit, name='edit'),
  path('product/delete/<int:id>/',productDelete, name='delete'),
  path('products/hide/',productsHidden,name='hide'),
  path('termsAndCondition/',termsAndConditions,name='terms')
]