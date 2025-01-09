from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload_document():
    try:
        file = request.files['document']
        if file:
            # Process and store the document securely
            # e.g., save to database or file system
            return jsonify({"message": "Document uploaded successfully"}), 200
        else:
            return jsonify({"error": "No file provided"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)