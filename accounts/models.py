from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from .managers import UserManager
from django.db import models

# Create your models here.
from django_otp.models import Device
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractBaseUser):
    personal_code = models.CharField(
        max_length=15,
        unique=True,
    )
    name = models.CharField(
        max_length=200,
    )
    mobile_number = PhoneNumberField(
        max_length=20,
        unique=True,
    )
    is_active = models.BooleanField(
        default=True,
    )
    is_superuser = models.BooleanField(
        default=False,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    created = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'personal_code'
    REQUIRED_FIELDS = ('name', 'mobile_number')
    objects = UserManager()

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.personal_code


class OTPVerify(models.Model):
    mobile_number = PhoneNumberField(
        unique=True,
    )
    code = models.IntegerField(
        null=True,
        blank=True,
    )
    generated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.mobile_number)

