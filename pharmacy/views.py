from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from customer.models import Customer
from .forms import PrescriptionForm
from .models import Prescription
from drug.models import Drug

# Create your views here.
# def index(request):
#     form = PrescriptionForm()
#     context = {'form': form}
#     return render(request, '', context)
from .utils import create_bot_link, create_qrcode, render_to_pdf


def index(request):
    print(request.GET)
    print('hi bitch')

    drugs = Drug.objects.all()
    form = PrescriptionForm()
    context = {'drugs': drugs, 'form': form}
    return render(request, 'pharmacy/drug_list.html', context)


# def search(request):

# Drug.objects.filter(Q(name_fa))

@csrf_exempt
@require_POST
def generate_prescription(request):
    print(request.POST)
    form = PrescriptionForm(request.POST)
    print('hv')
    if form.is_valid():
        print('valid')
        # save noskhe
        customer, created = Customer.objects.get_or_create(mobile_number=form.cleaned_data.get('mobile_number'))
        prescription = form.save(commit=False)
        prescription.customer = customer
        prescription.save()
        prescription.drugs.set(form.cleaned_data.get('drugs'))

        print(prescription.drugs)
        print('done')
        # create start bot
        # image = create_qrcode(prescription)
        link = create_bot_link(customer)
        # create qrcode

        # pass qrcode
        data = {
            'today': '13 Tir',
            'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        pdf = render_to_pdf('pdf/invoice.html', data)
        prescription.pdf_export = pdf
        prescription.save()

        return JsonResponse({'link': link})
    else:
        print('not valid')
        print(form.errors)
        return JsonResponse(data={'status': 403, 'msg': 'مشکلی وجود دارد.'})


def send_data(request):
    print('here')
    query = request.GET.get('q', None)
    if query:
        print('1')
        data = Drug.objects.filter(
            Q(name_en__contains=query) | Q(name_fa__contains=query) | Q(code__contains=query)).values('name_en',
                                                                                                      'name_fa', 'code')
    else:
        print('2')
        data = Drug.objects.values('name_en', 'name_fa', 'code')
    print(data)
    return JsonResponse(list(data), safe=False)
