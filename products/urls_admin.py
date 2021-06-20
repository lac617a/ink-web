from django.urls import path
from django.contrib.auth.decorators import login_required
from .views_admin import *

app_name="Admin"

urlpatterns = [
  path('list-products/',ListProdViewAdmin.as_view(),name="listProducts"),
  path('edit-products/<int:pk>/',UpdateProdViewAdmin.as_view(),name="editProducts"),
  path('add-products/',AddProdViewAdmin.as_view(),name="addProducts"),
  path('delete-products/<int:pk>/',DeleteProdViewAdmin.as_view(),name="deleteProducts"),
  #CRUD CON LAS CATEGORIAS AND MARCAS
  path('list-category/',ListCategoryView.as_view(),name="listCategory"),
  path('edit-category/<int:pk>/',UpdateCategoryView.as_view(),name="editCategory"),
  path('add-category/',AddCategoryView.as_view(),name="addCategory"),
  path('delete-category/<int:pk>/',DeleteCategoryView.as_view(),name="deleteCategory"),
  # MARCAS
  path('list-brand/',ListBrandView.as_view(),name="listBrand"),
  path('edit-brand/<int:pk>/',UpdateBrandView.as_view(),name="editBrand"),
  path('add-brand/',AddBrandView.as_view(),name="addBrand"),
  path('delete-brand/<int:pk>/',DeleteBrandView.as_view(),name="deleteBrand"),
]