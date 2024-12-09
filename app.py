from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes by default

# Public endpoint


@app.route('/helloPublic', methods=['GET'])
def say_hello_public():
    return jsonify({"message": "Hello From a public World!"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
