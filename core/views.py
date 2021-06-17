from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail

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

def admin(request):
  return render(request,'admin.html')