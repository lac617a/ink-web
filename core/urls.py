from django.urls import path
from .views import *

app_name="Main"

urlpatterns = [
  path('',windowMain, name='windowMain'),
  path('termsAndCondition/',termsAndConditions,name='terms'),
  path('maintenance/',maintenance,name='maintenance'),

  path('maintenance/preventive/',maintenancePreventive,name='preventive'),
  path('maintenance/preventive/computers/',maintenancePreventiveComputers,name='preventiveComputer'),
  path('maintenance/preventive/computers/<slug:slug>/',maintenancePreventiveAllComputers,name='preventiveComputerAll'),
  path('maintenance/preventive/printers/',maintenancePreventivePrinters,name='preventivePrinter'),
  path('maintenance/preventive/printers/<slug:slug>/',maintenancePreventiveAllPrinters,name='preventiveAllPrinter'),

  path('maintenance/corrective/',maintenanceCorrective,name='corrective'),
  path('maintenance/corrective/computers/',maintenanceCorrectiveComputers,name='correctiveComputer'),
  path('maintenance/corrective/computers/<slug:slug>/',maintenanceCorrectiveAllComputers,name='correctiveComputerAll'),
  path('maintenance/corrective/printers/',maintenanceCorrectivePrinters,name='correctivePrinter'),
  path('maintenance/corrective/printers/<slug:slug>/',maintenanceCorrectiveAllPrinters,name='correctiveAllPrinter'),
]