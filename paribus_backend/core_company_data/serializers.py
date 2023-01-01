from rest_framework import serializers
from .models import PriceData

class PriceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceData
        fields = ('ticker', 'timestamp', 'open', 'high', 'low', 'close', 'volume', 'market_cap', 'company_id')