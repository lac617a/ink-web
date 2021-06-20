from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from .models import Computer, Printer

# Create your views here.

def windowMain(request):
  if request.method == 'POST':
    subject = request.POST.get('subject')
    mail = request.POST.get('mail')
    message = request.POST.get('content') + f' |Remitente {mail}'
    gmail = settings.EMAIL_HOST_USER
    email_from = gmail

    recipent_list = [gmail]
    send_mail(subject,message,email_from,recipent_list)
    return redirect('/')
  return render(request,'home.html')

def termsAndConditions(request):
  return render(request,'termsAndCondition.html')

def maintenance(request):
  return render(request,'maintenance/maintenance.html')

def maintenancePreventive(request):
  return render(request,'maintenance/preventive/preventive.html')

def maintenanceCorrective(request):
  return render(request,'maintenance/corrective/corrective.html')




def maintenancePreventiveComputers(request):
  queryset = Computer.objects.all()
  return render(request,'maintenance/preventive/preventiveComputer/preventiveComputer.html',{'qs':queryset})

def maintenancePreventiveAllComputers(request,slug):
  queryset = Computer.objects.filter(name=slug)
  return render(request,'maintenance/preventive/preventiveComputer/preventiveAll.html',{'qs':queryset})

def maintenancePreventivePrinters(request):
  queryset = Printer.objects.all()
  return render(request,'maintenance/preventive/preventivePrinter/preventivePrinter.html',{'qs':queryset})

def maintenancePreventiveAllPrinters(request,slug):
  queryset = Printer.objects.filter(name=slug)
  return render(request,'maintenance/preventive/preventivePrinter/preventiveAll.html',{'qs':queryset})



def maintenanceCorrectiveComputers(request):
  queryset = Computer.objects.all()
  return render(request,'maintenance/corrective/correctiveComputer/correctiveComputer.html',{'qs':queryset})

def maintenanceCorrectiveAllComputers(request,slug):
  queryset = Computer.objects.filter(name=slug)
  return render(request,'maintenance/corrective/correctiveComputer/correctiveAll.html',{'qs':queryset})

def maintenanceCorrectivePrinters(request):
  queryset = Printer.objects.all()
  return render(request,'maintenance/corrective/correctivePrinter/correctivePrinter.html',{'qs':queryset})

def maintenanceCorrectiveAllPrinters(request,slug):
  queryset = Printer.objects.filter(name=slug)
  return render(request,'maintenance/corrective/correctivePrinter/correctiveAll.html',{'qs':queryset})