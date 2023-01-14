from django.test import TestCase
from .models import PriceData, CompanyCore
from datetime import datetime, timedelta

class PriceDataTestCase(TestCase):
    def setUp(self):
        # TODO: TEsts failing
        self.yesterday = datetime.today().date() - timedelta(days=1)
        self.day_before_yesterday = datetime.today().date() - timedelta(days=2)

        self.company = CompanyCore.objects.create(
            company_name='Tesla',
            home_country='United States',
            home_office='Palo Alto, California',
            is_public=True,
            ticker='TSLA'
        )


        self.data = {
            'ticker': 'TSLA',
            'timestamp': datetime.today().date(),
            'open': 100.0,
            'high': 105.0,
            'low': 95.0,
            'close': 100.0,
            'volume': 100,
            'company_id': self.company,
        }
        self.yesterday_data = {
            'ticker': 'TSLA',
            'timestamp': self.yesterday,
            'open': 90.0,
            'high': 95.0,
            'low': 85.0,
            'close': 90.0,
            'volume': 90,
            'company_id': self.company,
        }
        self.day_before_yesterday_data = {
            'ticker': 'TSLA',
            'timestamp': self.day_before_yesterday,
            'open': 80.0,
            'high': 85.0,
            'low': 75.0,
            'close': 80.0,
            'volume': 80,
            'company_id': self.company,
        }

    def test_save_with_yesterday_data(self):
        PriceData.objects.create(**self.yesterday_data)
        obj = PriceData.objects.create(**self.data)
        self.assertEqual(obj.daily_pct_change, 11.11111111111111)
        
    def test_save_without_yesterday_data(self):
        obj = PriceData.objects.create(**self.data)
        self.assertEqual(obj.daily_pct_change, None)

    def test_str_representation(self):
        obj = PriceData.objects.create(**self.data)
        self.assertEqual(str(obj), f"{self.data['ticker']}-{self.data['timestamp']}-{self.data['close']}")
    
    
    def test_multiple_objects(self):
        before_yesterday_obj = PriceData.objects.create(**self.day_before_yesterday_data)
        yesterday_obj = PriceData.objects.create(**self.yesterday_data)
        obj = PriceData.objects.create(**self.data)

        self.assertEqual(obj.daily_pct_change, 11.11111111111111)
        self.assertEqual(yesterday_obj.daily_pct_change, 12.5)

        self.assertEqual(obj.timestamp, datetime.today().date())
        self.assertEqual(yesterday_obj.timestamp, self.yesterday)
        self.assertEqual(before_yesterday_obj.timestamp, self.day_before_yesterday)
