# import smtplib

# from email.mime.text import MIMEText
# from django.conf import settings
# # Create your tests here.

# def send_email():
#   try:
#     # Establecemos conexion con el servidor smtp de gmail
#     mailServer = smtplib.SMTP(settings.EMAIL_HOST,settings.EMAIL_PORT)
#     mailServer.ehlo() 
#     mailServer.starttls()
#     mailServer.ehlo()
#     mailServer.login(settings.EMAIL_HOST_USER,settings.EMAIL_HOST_PASSWORD)
#     # Construimos el mensaje simple
#     mensaje = MIMEText("""Este es el mensaje de las narices""")
#     mensaje['From'] = settings.EMAIL_HOST_USER
#     mensaje['To'] = settings.EMAIL_HOST_USER
#     mensaje['Subject'] = "Tienes un correo"
#     # Envio del mensaje
#     mailServer.sendmail(settings.EMAIL_HOST_USER,settings.EMAIL_HOST_USER,mensaje.as_string())
#   except Exception as e:
#     print(e)

# send_email()