# Django Built-in modules
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, personal_code, name, mobile_number, password=None):
        print('reach here')
        if not personal_code:
            raise ValueError('کاربر باید کد پرسنلی داشته باشد.')
        if not name:
            raise ValueError('کاربر باید نام داشته باشد.')
        if not mobile_number:
            raise ValueError('کاربر باید شماره موبایل داشته باشد.')
        user = self.model(personal_code=personal_code, name=name, mobile_number=mobile_number)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, personal_code, name, password, mobile_number):
        user = self.create_user(personal_code, name, password, mobile_number)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
