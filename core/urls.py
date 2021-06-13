from django.urls import path
from .views import windowMain, termsAndConditions

app_name="Main"

urlpatterns = [
  path('',windowMain, name='windowMain'),
  path('termsAndCondition/',termsAndConditions,name='terms')
]