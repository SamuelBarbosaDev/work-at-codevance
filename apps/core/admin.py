from django.contrib import admin
from core.models import *

# Register your models here.
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    exclude = ()

@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    exclude = ()

@admin.register(Request)
class CompanyAdmin(admin.ModelAdmin):
    exclude = ()