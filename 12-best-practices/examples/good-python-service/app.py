import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.get('/')
def home():
    return jsonify({
        'service': os.getenv('APP_NAME', 'good-python-service'),
        'environment': os.getenv('APP_ENV', 'development'),
        'message': 'This example collects several Docker best practices in one small app.'
    })

@app.get('/health')
def health():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
