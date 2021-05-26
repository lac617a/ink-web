from django.shortcuts import render
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

# Create your views here.
def send_email(mail,content):
    context = {'mail':mail,'content':content}
    template = get_template('send_correo.html')
    content_template = template.render(context)
    email = EmailMultiAlternatives(
        "Un correo de prueba",
        "INK DYE soluciones integrales",
        settings.EMAIL_HOST_USER,
        [mail]
    )
    email.attach_alternative(content_template,'text/html')
    email.send()

def windowMain(request):
    if request.method == 'POST':
        mail = request.POST.get('mail')
        content = request.POST.get('content')

        send_email(mail,content)
    return render(request,'home.html')