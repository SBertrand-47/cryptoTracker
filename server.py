from flask import Flask, jsonify, render_template
from flask_cors import CORS
import requests
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route('/api/crypto', methods=['GET'])
def crypto_data():
    response = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,litecoin,dogecoin&vs_currencies=usd')
    data = response.json()

    crypto_data = [
        {"name": "Bitcoin", "price_usd": str(data["bitcoin"]["usd"])},
        {"name": "Ethereum", "price_usd": str(data["ethereum"]["usd"])},
        {"name": "Litecoin", "price_usd": str(data["litecoin"]["usd"])},
        {"name": "Dogecoin", "price_usd": str(data["dogecoin"]["usd"])}
    ]

    return jsonify(crypto_data)

@app.route('/api/crypto-history', methods=['GET'])
def crypto_history():
    cryptos = ["bitcoin", "ethereum", "litecoin", "dogecoin"]
    crypto_history_data = {}

    for crypto in cryptos:
        response = requests.get(f'https://api.coingecko.com/api/v3/coins/{crypto}/market_chart?vs_currency=usd&days=30')
        data = response.json()

        dates = [datetime.fromtimestamp(x / 1000).strftime('%Y-%m-%d') for x in data['prices'][::24][0]]
        prices = [y for x, y in data['prices'][::24]]

        crypto_history_data[crypto.capitalize()] = {"dates": dates, "prices": prices}

    return jsonify(crypto_history_data)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
