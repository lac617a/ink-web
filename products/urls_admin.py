from django.urls import path
from django.contrib.auth.decorators import login_required
from .views_admin import ListProdViewAdmin,UpdateProdViewAdmin,DeleteProdViewAdmin

app_name="Admin"

urlpatterns = [
  path('list-products/',ListProdViewAdmin.as_view(),name="list-products"),
  path('edit-products/<int:pk>/',UpdateProdViewAdmin.as_view(),name="edit-products"),
  path('delete-products/<int:pk>/',DeleteProdViewAdmin.as_view(),name="delete-products"),
]