
m flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/status', methods=['GET'])
def status():
    return jsonify({"status": "OK"})

# Ensure the following block is added to allow importing 'app' in a different file
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
