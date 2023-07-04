from django import forms

from customer.models import Customer
from .models import Prescription


class PrescriptionForm(forms.ModelForm):
    mobile_number = forms.CharField(widget=forms.NumberInput)
    class Meta:
        model = Prescription
        fields = ('drugs', )
    #
    # def clean(self):
    #     cleaned_data = super(PrescriptionForm, self).clean()
    #     self.set_values_for_customer(cleaned_data)
    #
    #
    #     return cleaned_data
    #
    # def save(self, commit=True):
    #     if not commit:


    # def set_values_for_customer(self, cleaned_data):
    #     print(cleaned_data)
    #     # if self.fo
    #     prescription, created = Prescription.objects.get_or_create(customer__mobile_number=cleaned_data['mobile_number'], drugs=cleaned_data['drugs'])
    #     print(prescription)

        # instance.customer = customer
        # print(instance)
        # print(instance.drugs)
        # # instance.drugs
        # print(commit)
        # if commit:
        #     instance.save()
        # instance.save()

        # mobile_number = self.cleaned_data.get('mobile_number')
        #
        # customer, created = Customer.objects.get_or_create(mobile_number=mobile_number)
        # print(customer)
        # print(self.cleaned_data)




