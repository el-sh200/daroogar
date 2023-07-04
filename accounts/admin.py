from django.contrib import admin

# Register your models here.
from accounts.models import User, OTPVerify

admin.site.register(User)
admin.site.register(OTPVerify)
