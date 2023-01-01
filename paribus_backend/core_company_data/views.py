from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PriceDataSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import PriceData
from .serializers import PriceDataSerializer

# Price data views:
@api_view(['GET'])
def get_price_data(request):

    ticker = request.query_params.get('ticker')
    queryset = PriceData.objects.filter(ticker=ticker)    
    
    serializer = PriceDataSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_price_data(request):
    serializer = PriceDataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

