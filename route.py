import subprocess
from flask import Flask, jsonify, request
import os

# Create Flask app
app = Flask(__name__)

def allowed_file(filename):
    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

# Define a route for uploading images
@app.route('/api/upload', methods=['POST'])
def upload_file():
    # Check if the request contains a file
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    # Check if the file name is empty
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    # Check if the file has an allowed extension
    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file format. Only PNG, JPG, JPEG, and GIF are allowed.'})

    # Save the file to a specific location
    file.save(os.path.join('images', file.filename))
    result = subprocess.run(f"python astrometry.net/net/client/client.py -k zlwawjrthmpelnsq -u images/{file.filename}", shell = True, executable="/bin/bash", capture_output=True, text=True)

    return jsonify({'message': result.stdout})


# Run the app on port 80
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
