from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives

from django.conf import settings

def send_email_contact(mail, nombre, correo, mensage, telefono):
    context = {
        'mail': mail,
        'nombre': nombre,
        'correo': correo,
        'mensaje': mensage,
        'telefono': telefono
        }    
    template = get_template('contact/email.html')
    content = template.render(context)
    email = EmailMultiAlternatives(
        'Soporte',
        '',
        settings.EMAIL_HOST_USER,
        [mail]
    )
    email.attach_alternative(content, 'text/html')
    email.send()