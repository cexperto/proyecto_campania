from io import BytesIO
from re import template # nos ayuda a convertir un html en pdf
from django.http import HttpResponse
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from xhtml2pdf import pisa
from django.conf import settings

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def send_email(mail):
    context = {'mail': mail}    
    template = get_template('users/email.html')
    content = template.render(context)
    email = EmailMultiAlternatives(
        'Gracias por inscribirte',
        '',
        settings.EMAIL_HOST_USER,
        [mail]
    )
    email.attach_alternative(content, 'text/html')
    email.send()