from django.db import models

# Create your models here.
from customer.models import Customer
from drug.models import Drug


class Prescription(models.Model):
    drugs = models.ManyToManyField(Drug)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    pdf_export = models.FileField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
