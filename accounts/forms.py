# Django Built-in modules
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import gettext_lazy as _

# Local apps
from .models import User, OTPVerify

# Third Party Packages
from phonenumber_field.formfields import PhoneNumberField


# Start Admin Panel Forms #

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label=_('رمز عبور'),
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label=_('تکرار رمز عبور'),
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = (
            'personal_code',
            'name',
            'mobile_number',
            'is_superuser',
            'is_staff',
            'is_active',
        )

    def clean_password2(self):
        cd = self.cleaned_data
        if not cd['password1'] or not cd['password2']:
            raise forms.ValidationError(_('این فیلد الزامی است.'))
        elif cd['password1'] != cd['password2']:
            raise forms.ValidationError(_('رمز عبور و تکرار آن مطابقت ندارد.'))
        return cd['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        label=_('رمز عبور'),
        help_text=_(
            "رمزهای عبور خام ذخیره نمی شوند، بنابراین راهی برای دیدن رمز عبور این کاربر وجود ندارد، اما می توانید رمز عبور را با استفاده از <a href=\"../password/\">این فرم</a> تغییر دهید."
        ),
    )

    class Meta:
        model = User
        fields = (
            'personal_code',
            'name',
            'mobile_number',
            'is_superuser',
            'is_staff',
            'is_active',
        )

    def clean_password(self):
        return self.initial['password']


# End Admin Panel Forms #


# Start Login and Register Forms #

class UserLoginForm(forms.ModelForm):
    otp_code = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = (
            'mobile_number',
            'personal_code',
        )
        widgets = {
            'mobile_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شماره موبایل'}),
            'personal_code': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'کد پرسنلی'}),
        }

    def clean_mobile_number(self):
        mobile_number = self.cleaned_data['mobile_number']
        mobile_number = str(mobile_number).replace(' ', '')
        return mobile_number

    def clean(self):
        cleaned_data = self.cleaned_data
        print(cleaned_data)
        mobile_number = cleaned_data['mobile_number']
        mobile_number = str(mobile_number).replace(' ', '')
        personal_code = cleaned_data['personal_code']
        try:
            user = User.objects.get(personal_code=personal_code, mobile_number=mobile_number)
            if not user:
                raise forms.ValidationError('کاربری با این کد پرسنلی و شماره موبایل موجود نیست.')
        except User.DoesNotExist as e:
            raise forms.ValidationError('کاربر یافت نشد.')
        return cleaned_data


class UserRegisterForm(forms.ModelForm):
    otp_code = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = (
            'mobile_number',
            'personal_code',
            'name'
        )
        widgets = {
            'mobile_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شماره موبایل'}),
            'personal_code': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'کد پرسنلی'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام'}),
        }

    def clean_mobile_number(self):
        print('in clean mobile')
        mobile_number = self.cleaned_data['mobile_number']
        mobile_number = str(mobile_number).replace(' ', '')
        user = User.objects.filter(mobile_number=mobile_number)
        if user.exists():
            print('raise mobile_number')
            raise forms.ValidationError(_('این شماره قبلا ثبت نام کرده است.'))
        return mobile_number

    def clean_personal_code(self):
        personal_code = self.cleaned_data['personal_code']
        user = User.objects.filter(personal_code=personal_code)
        if user.exists():
            raise forms.ValidationError('این کد پرسنلی قبلا ثبت نام کرده است.')
        return personal_code

    def clean(self):
        print('in clean all')
        cleaned_data = self.cleaned_data
        print(cleaned_data)
        otp_code = cleaned_data['otp_code']
        mobile_number = cleaned_data['mobile_number']
        mobile_number = str(mobile_number).replace(' ', '')
        print(mobile_number)
        verify = OTPVerify.objects.get(mobile_number=mobile_number)
        print(verify.code)
        if verify.code != otp_code:
            raise forms.ValidationError('کد اشتباه است.')
        return cleaned_data
