import smtplib

# from django.conf import settings
from django.test import TestCase
from email.mime.text import MIMEText
from config.settings import EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER,EMAIL_HOST_PASSWORD

# Create your tests here.

def send_email():
  try:
    # Establecemos conexion con el servidor smtp de gmail
    mailServer = smtplib.SMTP(EMAIL_HOST,EMAIL_PORT)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(EMAIL_HOST_USER,EMAIL_HOST_PASSWORD)
    # Construimos el mensaje simple
    mensaje = MIMEText("""Este es el mensaje de las narices""")
    mensaje['From'] = EMAIL_HOST_USER
    mensaje['To'] = EMAIL_HOST_USER
    mensaje['Subject'] = "Tienes un correo"
    # Envio del mensaje
    mailServer.sendmail(EMAIL_HOST_USER,EMAIL_HOST_USER,mensaje.as_string())
  except Exception as e:
    print(e)

send_email()