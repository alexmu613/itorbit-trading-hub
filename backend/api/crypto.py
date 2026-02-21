from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

BINANCE_API_URL = 'https://api.binance.com/api'

@app.route('/api/crypto/<symbol>', methods=['GET'])
def get_crypto_data(symbol):
    try:
        response = requests.get(f'{BINANCE_API_URL}/v3/ticker/price?symbol={symbol.upper()}')
        
        if response.status_code == 200:
            return jsonify(response.json()), 200
        else:
            return jsonify({'error': 'Failed to fetch data from Binance'}), response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)