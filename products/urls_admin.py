from django.urls import path
from django.contrib.auth.decorators import login_required
from .views_admin import *

app_name="Admin"

urlpatterns = [
  path('list-products/',login_required(ListProdViewAdmin.as_view()),name="listProducts"),
  path('edit-products/<int:pk>/',login_required(UpdateProdViewAdmin.as_view()),name="editProducts"),
  path('add-products/',login_required(AddProdViewAdmin.as_view()),name="addProducts"),
  path('delete-products/<int:pk>/',login_required(DeleteProdViewAdmin.as_view()),name="deleteProducts"),
  #CRUD CON LAS CATEGORIAS AND MARCAS
  path('list-category/',login_required(ListCategoryView.as_view()),name="listCategory"),
  path('edit-category/<int:pk>/',login_required(UpdateCategoryView.as_view()),name="editCategory"),
  path('add-category/',login_required(AddCategoryView.as_view()),name="addCategory"),
  path('delete-category/<int:pk>/',login_required(DeleteCategoryView.as_view()),name="deleteCategory"),
  # MARCAS
  path('list-brand/',login_required(ListBrandView.as_view()),name="listBrand"),
  path('edit-brand/<int:pk>/',login_required(UpdateBrandView.as_view()),name="editBrand"),
  path('add-brand/',login_required(AddBrandView.as_view()),name="addBrand"),
  path('delete-brand/<int:pk>/',login_required(DeleteBrandView.as_view()),name="deleteBrand"),
]