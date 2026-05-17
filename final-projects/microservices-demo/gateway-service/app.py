import os
from urllib.request import urlopen
from flask import Flask, jsonify

app = Flask(__name__)

@app.get('/')
def home():
    product_service_url = os.getenv('PRODUCT_SERVICE_URL', 'http://product-service:5000')
    with urlopen(f'{product_service_url}/products', timeout=5) as response:
        products_json = response.read().decode('utf-8')
    return jsonify({
        'message': 'Gateway service response',
        'product_service_url': product_service_url,
        'products_raw_json': products_json,
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
