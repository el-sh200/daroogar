from django.db import models


# Create your models here.
class Customer(models.Model):
    mobile_number = models.CharField(
        max_length=20,
    )
    telegram_uid = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )
