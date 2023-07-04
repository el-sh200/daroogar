from qrcode import *

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa

BOT_USERNAME = 'daroogar_bot'


def create_bot_link(customer):
    url = f'https://t.me/{BOT_USERNAME}?start=c{customer.mobile_number}'
    return url


def create_qrcode(prescription):
    img = make(create_bot_link(prescription.customer))
    img.save(f"media/qrcodes/num_{prescription.id}.png")
    return img


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None
