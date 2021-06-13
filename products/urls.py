from django.urls import path
from .views import productsViews,productDelete,productEdit,productsHidden

app_name="Product"

urlpatterns = [
  path('',productsViews,name='pro'),
  path('superadmin/edit/<int:id>/',productEdit, name='edit'),
  path('superadmin/delete/<int:id>/',productDelete, name='delete'),
  path('superadmin/hide/',productsHidden,name='hide'),
]