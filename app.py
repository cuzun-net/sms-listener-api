from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple in-memory storage (will be reset when server restarts)
latest_payload = None

@app.route('/api/data', methods=['POST', 'GET'])
def handle_data():
    global latest_payload
    
    if request.method == 'POST':
        # Store the incoming JSON payload
        latest_payload = request.get_json()
        return jsonify({"message": "Data stored successfully"}), 201
    
    elif request.method == 'GET':
        # Return the latest stored payload
        if latest_payload is None:
            return jsonify({"message": "No data stored yet"}), 404
        return jsonify(latest_payload), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
