from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Configure your ExchangeRate-API key and URL here
API_KEY = 'YOUR_API_KEY'
API_URL = 'https://v6.exchangerate-api.com/v6/{}/{}'

@app.route('/forex/latest', methods=['GET'])
def get_latest_forex():
    base_currency = request.args.get('base', 'USD')  # Default to USD if no base is provided
    response = requests.get(API_URL.format(API_KEY, 'latest/{}'.format(base_currency)))
    return jsonify(response.json())

@app.route('/forex/history', methods=['GET'])
def get_forex_history():
    base_currency = request.args.get('base', 'USD')
    target_currency = request.args.get('target')
    date = request.args.get('date')  # Expecting YYYY-MM-DD format
    if not target_currency or not date:
        return jsonify({'error': 'target and date parameters are required.'}), 400
    response = requests.get(API_URL.format(API_KEY, 'historical/{}/{}'.format(date, base_currency)))
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)