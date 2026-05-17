import os
import psycopg
from flask import Flask, jsonify

app = Flask(__name__)

def get_connection():
    return psycopg.connect(
        host=os.getenv('DB_HOST', 'db'),
        dbname=os.getenv('DB_NAME', 'course_db'),
        user=os.getenv('DB_USER', 'course_user'),
        password=os.getenv('DB_PASSWORD', 'course_pass'),
    )

@app.get('/')
def home():
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute('SELECT version()')
            version = cursor.fetchone()[0]
    return jsonify({
        'message': 'Flask and PostgreSQL are running in Docker Compose',
        'postgres_version': version,
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
