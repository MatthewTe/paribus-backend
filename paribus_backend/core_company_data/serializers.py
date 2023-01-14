from rest_framework import serializers
from .models import PriceData, CompanyCore

class PriceDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = PriceData
        fields = ('ticker', 'timestamp', 'open', 'high', 'low', 'close', 'volume', 'company_id')

class CompanyCoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyCore
        fields = ('id', 'company_name', 'home_country', 'home_office', 'is_public', 'ticker')