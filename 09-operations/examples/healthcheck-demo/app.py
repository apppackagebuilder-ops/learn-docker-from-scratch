import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.get('/')
def home():
    app.logger.info('Home endpoint was called')
    return jsonify({'message': 'Operations demo is running'})

@app.get('/health')
def health():
    status = os.getenv('APP_STATUS', 'ok')
    if status != 'ok':
        return jsonify({'status': status}), 500
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
