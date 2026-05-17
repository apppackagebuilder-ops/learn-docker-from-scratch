from flask import Flask, jsonify

app = Flask(__name__)

@app.get('/products')
def products():
    return jsonify([
        {'id': 1, 'name': 'Laptop Stand'},
        {'id': 2, 'name': 'USB-C Dock'},
        {'id': 3, 'name': 'Mechanical Keyboard'}
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
