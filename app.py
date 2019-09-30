import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from flask import send_from_directory

UPLOAD_FOLDER = 'C:/Users/KR/PycharmProjects/Automated_Note_Maker'
ALLOWED_EXTENSIONS = {'mp3', 'wav', 'dct'}

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

path = 'C:/Users/KR/PycharmProjects/Automated_Note_Maker'
c_mat = os.listdir(path)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    print("check")
    if request.method == 'POST':
        print("check1")
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            #filename = request.files['file']
            #filename.save(secure_filename(file.filename))
            print("check2")
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            return redirect(url_for('uploaded_file'))
    return render_template('screen1.html')

@app.route('/uploads')
def uploaded_file(filename):
    print("check3")
    #return send_from_directory(app.config['UPLOAD_FOLDER'],  filename)
    return render_template('file_upload_result.html')

if __name__ == "__main__":
    app.run( debug=True)