import uuid
from django.db import models

class CompanyCore(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_name = models.CharField(max_length=100, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, blank=True)
    home_country = models.CharField(max_length=50)
    home_office = models.CharField(max_length=200)
    is_public = models.BooleanField(blank=True)
    
    class Meta:
        verbose_name = "Core Company Metadata"
        verbose_name_plural = "Companies"
