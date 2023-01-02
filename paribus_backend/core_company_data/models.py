import uuid
from django.db import models

class CompanyCore(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_name = models.CharField(max_length=100, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, blank=True)
    home_country = models.CharField(max_length=50)
    home_office = models.CharField(max_length=200)
    is_public = models.BooleanField(blank=True)
    ticker = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.company_name}-{self.id}"

    class Meta:
        verbose_name = "Core Company Metadata"
        verbose_name_plural = "Companies"


class PriceData(models.Model):
    ticker = models.CharField(max_length=10)
    timestamp = models.DateTimeField(unique=True)
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.PositiveIntegerField()
    company_id = models.ForeignKey(CompanyCore, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ticker}-{self.timestamp}-{self.close}"

    class Meta:
        verbose_name = "Company Price Timeseries"

