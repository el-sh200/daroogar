from django.contrib import admin
from .models import Drug

# Register your models here.
@admin.register(Drug)
class DrugAdmin(admin.ModelAdmin):
    search_fields = ('name_fa', 'description',)
