from django.db.models import Q
from django.http import JsonResponse, HttpResponse
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
    print('hi')

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
    if form.is_valid():
        customer, created = Customer.objects.get_or_create(mobile_number=form.cleaned_data.get('mobile_number'))
        prescription = form.save(commit=False)
        prescription.customer = customer
        prescription.save()
        prescription.drugs.set(form.cleaned_data.get('drugs'))
        link = create_bot_link(customer)
        response = render_to_pdf('pharmacy/pdf.html', {'prescription': prescription})
        rr = HttpResponse(response, content_type='application/pdf')
        address = f'media/'

        file_name = f'prescription/pre-{prescription.id}.pdf'
        try:
            f = open(address+file_name, 'wb')
            f.write(rr.content)
            f.close()
        except Exception as e:
            pass
        prescription.pdf_export = file_name
        prescription.save()

        return JsonResponse({'link': link})
    else:
        print('not valid')
        print(form.errors)
        return JsonResponse(data={'status': 403, 'msg': 'مشکلی وجود دارد.'})


def send_data(request):
    query = request.GET.get('q', None)
    if query:
        data = Drug.objects.filter(
            Q(name_en__contains=query) | Q(name_fa__contains=query) | Q(code__contains=query)).values('id', 'name_en',
                                                                                                      'name_fa', 'code')
    else:
        data = Drug.objects.values('id', 'name_en', 'name_fa', 'code')
    return JsonResponse(list(data), safe=False)
