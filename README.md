# Crypto Tracker

This is a Flask web application that fetches and displays cryptocurrency prices and their 30-days history from the Coingecko API.

## Features

- Fetches the current prices of Bitcoin, Ethereum, Litecoin, and Dogecoin in USD.
- Fetches the last 30 days price history of Bitcoin, Ethereum, Litecoin, and Dogecoin in USD.
- Provides API endpoints to fetch this data.

## API Endpoints

- `/api/crypto`: Returns the current prices of Bitcoin, Ethereum, Litecoin, and Dogecoin in USD.
- `/api/crypto-history`: Returns the last 30 days price history of Bitcoin, Ethereum, Litecoin, and Dogecoin in USD.

## Prerequisites

- Python 3.x
- Flask
- Flask-CORS
- requests

## Installation

1. Clone the repository
2. Navigate to the directory
3. Install the dependencies
4. Run the application

The application will start running on `http://127.0.0.1:5000/`.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the terms of the MIT license.
