from flask import Flask

app = Flask(__name__)

@app.get('/')
def home():
    return {
        'message': 'Hello from a Flask app running in Docker',
        'course': 'Docker for Beginners'
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
