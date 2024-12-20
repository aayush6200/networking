from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes by default

# Public endpoint
@app.route('/health')
def health():
    return "Healthy", 200

@app.route('/helloPrivate', methods=['GET'])
def say_hello_private():
    return jsonify({"message": "Hello From a private World!"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
