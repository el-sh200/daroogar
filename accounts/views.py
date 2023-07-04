from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .forms import UserRegisterForm, UserLoginForm

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render

from .models import User
from .utils import send_sms


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            personal_code = cd.get('personal_code')
            mobile_number = cd.get('mobile_number')
            otp_code = cd.get('otp_code')

            user = authenticate(request, personal_code=personal_code, mobile_number=mobile_number, otp_code=otp_code)
            print(personal_code, mobile_number)
            ii = User.objects.get(personal_code=personal_code, mobile_number=mobile_number)
            print('user: ', ii)
            print(user)
            if user:
                login(request, user, backend='accounts.authentication.CustomAuthenticationBackend')
                print('yes')
                return redirect('pharmacy:index')
            else:
                print('error here')
        print(form.errors)
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data

            user = User.objects.create_user(name=cd['name'], mobile_number=cd['mobile_number'],
                                            personal_code=cd['personal_code'])
            login(request, user, backend='accounts.authentication.CustomAuthenticationBackend')
            return redirect('pharmacy:index')
        print(form.errors)

    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


@csrf_exempt
@require_POST
def send_otp(request):
    print(request.POST)
    mobile_number = request.POST.get('mobile_number')
    mobile_number = str(mobile_number).replace(' ', '')
    try:
        send_sms(mobile_number)
        return JsonResponse(data={'status': 200, 'message': 'پیامک حاوی کد تایید ارسال شد.'})
    except Exception as e:
        print(e)
        return JsonResponse(
            data={'status': 500, 'message': 'مشکلی در ارسال پیامک وجود دارد. لطفا با پشتیبانی تماس بگیرید.'})


def user_logout(request):
    logout(request)
    return redirect('accounts:user_login')
