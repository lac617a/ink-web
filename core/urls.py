from django.urls import path
from .views import windowMain

app_name="Main"

urlpatterns = [path('',windowMain, name='windowMain')]