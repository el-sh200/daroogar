from django.db import models


# Create your models here.
class Customer(models.Model):
    mobile_number = models.CharField(
        max_length=20,
        unique=True,
    )
    telegram_uid = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )
    has_visit_telegram = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return f"{self.mobile_number}"
