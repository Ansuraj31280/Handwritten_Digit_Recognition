from flask import Flask, render_template, request, redirect, url_for
from utils.ocr_utils import predict_digit
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            digit = predict_digit(filepath)
            return render_template('index.html', digit=digit)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
