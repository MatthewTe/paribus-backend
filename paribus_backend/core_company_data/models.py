import uuid
from django.db import models

import datetime

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
    timestamp = models.DateField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.PositiveIntegerField()
    company_id = models.ForeignKey(CompanyCore, on_delete=models.CASCADE)
    price_ticker_id = models.CharField(unique=True, max_length=200)

    # Need some metrics that measures 
    # - Support
    # - Resistance  
    # - Volume
    # - Momentum
    daily_pct_change = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.ticker}-{self.timestamp}-{self.close}"

    # TODO: Modify save function to add easily calculable technical indicators like pct change to the Model.
    # - Daily pct change 
    def save(self, *args, **kwargs):

        # Generating the unique priec ticker id for the price entry:
        self.price_ticker_id = f"{self.ticker}-{self.timestamp}"

        # When open, high, low, close data is added. try to query yesterdays ohlc
        yesterday = self.timestamp - datetime.timedelta(days=1)

        try:
            yesterdays_price_data = PriceData.objects.get(timestamp=yesterday, ticker=self.ticker)
        
        except PriceData.DoesNotExist:
            yesterdays_price_data = None

        # Using the previous value to calculate the daily percent change:
        # If there is a previous day, use ther closing price to calc the percent change and save it.
        if yesterdays_price_data is not None:
            self.daily_pct_change = (self.close - yesterdays_price_data.close)/yesterdays_price_data.close * 100
        else:
            self.daily_pct_change = None

        # if the queryset is empty set all the technical indicator fields to blank/null
        
        super(PriceData, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Company Price Timeseries"
        ordering = ["-timestamp"]

