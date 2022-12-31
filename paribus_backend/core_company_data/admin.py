from django.contrib import admin

from core_company_data.models import CompanyCore, PriceData

admin.site.register(CompanyCore)
admin.site.register(PriceData)