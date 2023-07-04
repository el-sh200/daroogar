from qrcode import *

BOT_USERNAME = 'daroogar_bot'


def create_bot_link(customer):
    url = f'https://t.me/{BOT_USERNAME}?start=c{customer.mobile_number}'
    return url


def create_qrcode(prescription):
    img = make(create_bot_link(prescription.customer))
    img.save(f"media/qrcodes/num_{prescription.id}.png")
    return img
