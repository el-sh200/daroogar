from django.db import models


# Create your models here.

class Drug(models.Model):
    name_fa = models.CharField(
        max_length=200,
    )
    name_en = models.CharField(
        max_length=200,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name_fa
