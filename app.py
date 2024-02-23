from flask import Flask, request, render_template
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}
PASSWORD = '12345'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = 'pdf'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def check_password(password):
    return password == PASSWORD

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files or 'password' not in request.form:
        return 'Invalid request'

    file = request.files['file']
    password = request.form['password']

    if file.filename == '' or not allowed_file(file.filename) or not check_password(password):
        if file.filename != '':
            # Delete the invalid file
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        return render_template('index.html', message='Invalid file or password')

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    result_message = os.popen(f'python3 process_file.py "{file_path}" "{app.config["PROCESSED_FOLDER"]}"').read()

    return render_template('index.html', message=result_message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
