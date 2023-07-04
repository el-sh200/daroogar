from accounts.models import OTPVerify
from random import randint

def send_sms(mobile_number):
    # something for sending sms
    verify, created = OTPVerify.objects.get_or_create(mobile_number=mobile_number)

    random_number = randint(100000, 999999)  # randint is inclusive at both ends
    print(random_number)
    verify.code = random_number
    verify.save()

    print('sending sms')
    return
