import requests
import json
import yfinance as yf
from flask import Flask, request

app = Flask(__name__)

@app.route('/get-price-data/<ticker>')
def get_price_data(ticker):

    # TODO: Develop logic for the endpoint

    # Get the endpoint and date range from the request parameters
    endpoint = request.args.get('endpoint')
    min_date_range = request.args.get('min_date_range')
    max_date_range = request.args.get('max_date_range')

    print(endpoint, min_date_range, max_date_range, ticker)

    # Get the stock info for the company
    #stock = yf.Ticker(ticker)

    # Get the historical price data for the company
    #df = stock.history(start=min_date_range, end=max_date_range)

    # Serialize the price data time-series into JSON
    #data = df.to_json(orient='records')
    
    # Make a POST request to the Django API with the price data
    #response = requests.post(endpoint, json=data)

    return f"{endpoint, min_date_range, max_date_range, ticker}"