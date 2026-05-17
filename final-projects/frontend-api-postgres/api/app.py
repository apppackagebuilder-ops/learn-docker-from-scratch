import os
import psycopg
from flask import Flask, jsonify

app = Flask(__name__)


def get_connection():
    return psycopg.connect(
        host=os.getenv('DB_HOST', 'db'),
        dbname=os.getenv('DB_NAME', 'storedb'),
        user=os.getenv('DB_USER', 'storeuser'),
        password=os.getenv('DB_PASSWORD', 'storepass'),
    )


@app.get('/api/health')
def health():
    return jsonify({'status': 'ok'})


@app.get('/api/products')
def products():
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute('SELECT id, name, description, price FROM products ORDER BY id')
            rows = cursor.fetchall()
    return jsonify({
        'products': [
            {
                'id': row[0],
                'name': row[1],
                'description': row[2],
                'price': str(row[3]),
            }
            for row in rows
        ]
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
