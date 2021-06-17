from django.urls import path
from .views import MoreViewDetailProd,ListProdView,GetCategoryProduView,GetBrandsProduView

app_name="Product"

urlpatterns = [
  path('list-products/',ListProdView.as_view(),name='list-products'),
  path('more-view/<int:pk>/',MoreViewDetailProd.as_view(),name='more-view'),
  path('get-category-view/<slug:slug>/',GetCategoryProduView.as_view(),name='get-category-view'),
  path('get-brands-view/<slug:slug>/',GetBrandsProduView.as_view(),name='get-brands-view'),
]