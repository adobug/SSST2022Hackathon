from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/adobug/Projects/webuploads'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('MedSite.html')

@app.route('/login')
def login():
    return render_template('Login.html')

"""
@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'
"""

if __name__ == "__main__":
    app.run(debug=True)