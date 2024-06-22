import os
from flask import Flask, request
from werkzeug.utils import secure_filename
from valid_db import valid_db


#openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/serv', methods=['POST'])
def get_example():
    mod = request.form.get('mod')

    if 'image' not in request.files:
        return 'No file part', 400

    file = request.files['image']
    if file.filename == '':
        return 'No selected file', 400

    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        if mod == 'valid':
            result = valid_db(file_path)
            return result
        else:
            return 'Invalid mod parameter', 400

    return 'Something went wrong', 500

if __name__ == '__main__':
    app.run(ssl_context=('cert.pem', 'key.pem'), host='0.0.0.0', port=5000, debug=True)
