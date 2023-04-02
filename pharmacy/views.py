from django.db.models import Q
from django.shortcuts import render
# from .forms import PrescriptionForm
from .models import Prescription
from drug.models import Drug

# Create your views here.
# def index(request):
#     form = PrescriptionForm()
#     context = {'form': form}
#     return render(request, '', context)

def index(request):
    drugs = Drug.objects.all()

    context = {'drugs': drugs}
    return render(request, 'pharmacy/drug_list.html', context)
# def search(request):

    # Drug.objects.filter(Q(name_fa))