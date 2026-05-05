from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"service": "StreamNest Content Catalog API", "status": "running", "version": "1.0"})

@app.route('/catalog')
def catalog():
    return jsonify({"contents": [
        {"id": "C101", "title": "The Last Horizon", "genre": "Sci-Fi", "duration": 7200},
        {"id": "C102", "title": "City of Storms", "genre": "Drama", "duration": 5400},
        {"id": "C103", "title": "Wild Frontiers", "genre": "Documentary", "duration": 3600},
        {"id": "C104", "title": "Neon Nights", "genre": "Thriller", "duration": 6300}
    ]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
