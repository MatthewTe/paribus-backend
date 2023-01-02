from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets, status
from .serializers import PriceDataSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import PriceData, CompanyCore
from .serializers import PriceDataSerializer

import requests
import datetime

# Price data views:
@api_view(['GET'])
def get_price_data(request):

    ticker = request.query_params.get('ticker')
    queryset = PriceData.objects.filter(ticker=ticker)    
    
    serializer = PriceDataSerializer(queryset, many=True)
    return Response(serializer.data)

# TODO: Determine how to handle duplicate values being written to the database
# - Will have to add logic to create a unique timestamp + ticker symbol/ company id to make sure that more than one ticker can be written to the database
@api_view(['POST'])
def create_price_data(request):
    """The logic that handels the POST request from the flask microservice which writes stock price data to the database
    using the PriceData data model. 

    The Django model has the following schema:
        ticker = models.CharField(max_length=10)
        timestamp = models.DateTimeField()
        open = models.FloatField()
        high = models.FloatField()
        low = models.FloatField()
        close = models.FloatField()
        volume = models.PositiveIntegerField()
        market_cap = models.BigIntegerField()
        company_id = models.ForeignKey(CompanyCore, on_delete=models.CASCADE)

    and the POST request comes in the following form:
    {
        ticker: TSLA,
        data: [
            {"Date":1663300800000,
            "Open":299.6099853516,"
            High":303.7099914551,
            "Low":295.6000061035,
            "Close":303.3500061035,
            "Volume":87087800,
            "Dividends":0.0,
            "Stock Splits":0.0}
        ]
    } 

    It writes data to the PriceData model using the PriceDataSerializer model seralizer.
    """
    # get the data from the request
    data = request.data

    # get the ticker from the request
    ticker = data['ticker']

    # get the company id from the database
    company_id = CompanyCore.objects.get(ticker=ticker).id

    # get the data from the request
    data = data['data']

    # create a list to store the data
    price_data = [
        {
        'ticker': ticker,
        'timestamp':datetime.datetime.fromtimestamp(datum["Date"]/1000).strftime('%Y-%m-%d'),
        'open': datum['Open'],
        'high': datum['High'],
        'low': datum['Low'],
        'close': datum['Close'],
        'volume': datum['Volume'],
        'company_id': company_id
        } for datum in data
    ]

    # create a serializer to write the data to the database
    serializer = PriceDataSerializer(data=price_data, many=True)
    
    # check if the serializer is valid
    if serializer.is_valid():
        # save the serializer
        serializer.save()

        # return a success message
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # return an error message
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Ping method for the flask microservice: 
def ping_microservice(request):
    # Send a GET request to the Flask microservice
    response = requests.get('http://flask-stock-price-microservice:5001/ping')
    
    # Return the response from the Flask microservice as a JSON response
    return JsonResponse(response.json())



# Request method that makes request to the microserivice to get it to make a POST request to the create_price_data view to write stock price data:
def write_stock_price_data(request):

    # Making ping request to the microservice to get status:
    microservice_status = requests.get("http://flask-stock-price-microservice:5001/ping")

    if microservice_status.status_code == 200:
        # Tasking the microservice to write stock price data to the database through the POST request:
        price_ingestion_endpoint = "http://django-backend:8000/stock/price-data/create/"
        
        # Determining what the start date fof the stock price data will be based on existing records in the database:
        existing_price_data = PriceData.objects.filter(ticker="TSLA")

        # If the queryset is empty, set the start_date to 2008-01-01:
        if not existing_price_data:
            start_date = datetime.datetime(2008, 1, 1)

        else:
            start_date = existing_price_data.order_by('-timestamp')[0].timestamp + datetime.timedelta(days=1)
            
        # Convert the timestamp value which is a DateTimeField into a date in the format: yyyy-mm-dd
        start_date = start_date.date()
        end_date = datetime.datetime.now().date()

        # Making request to the microservice to write price data:
        url_params = {
            "endpoint": price_ingestion_endpoint,
            "min_date_range": start_date,
            "max_date_range": end_date
        }

        # Making GET request to the microservice to write price data w the following values as url params:
        response = requests.get(url="http://flask-stock-price-microservice:5001/get-price-data/TSLA", params=url_params)
        #print(response.text)

        return JsonResponse(response.json(), safe=False)

    else:
        pass 