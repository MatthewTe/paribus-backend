import requests
import json
import yfinance as yf
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ping')
def ping():

    # Return the status and Flask app information in a JSON response
    return jsonify({
        'status': 'OK',
        'app_name': app.name,
    })

@app.route('/get-price-data/<ticker>')
def get_price_data(ticker):

    # TODO: Develop logic for the endpoint
    # - Process the endpoint and the minimum date range. 

    # Get the endpoint and date range from the request parameters
    endpoint = request.args.get('endpoint')
    min_date_range = request.args.get('min_date_range')
    max_date_range = request.args.get('max_date_range')

    # Get the stock info for the company
    stock = yf.Ticker(ticker)

    # Get the historical price data for the company
    df = stock.history(start=min_date_range, end=max_date_range).reset_index()

    # Serialize the price data time-series into JSON
    data = df.to_json(orient='records')
    json_data = json.loads(data)

    # Making a post request to the endpoint to write data:
    post_request = requests.post(endpoint, json={"ticker":ticker, "data":json_data})

    return post_request.text