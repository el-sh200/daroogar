
from django.contrib.auth.backends import BaseBackend

from .models import User, OTPVerify


class CustomAuthenticationBackend(BaseBackend):
    def authenticate(self, request, mobile_number=None, personal_code=None, otp_code=None, **kwargs):
        try:
            user = User.objects.get(mobile_number=mobile_number, personal_code=personal_code)
            otp = OTPVerify.objects.get(mobile_number=mobile_number)
            if otp.code == otp_code:
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
