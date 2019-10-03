import os
from flask import Flask, flash, request, redirect, url_for, render_template, send_file
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
    if request.method == 'POST':
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
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            return redirect(url_for('uploaded_file'))
    return render_template('screen1.html')

static_path = os.path.join(os.path.abspath("app"), "static")

@app.route('/download', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def downloadFile ():
    if request.method == 'GET':
        choice = request.form.get('choice')
        #print(choice)
        if choice == 'Transcript':
            #path1 = 'C:/Users/KR/PycharmProjects/Automated_Note_Maker/msft.txt'
            path = static_path + '/msft.txt'
        elif choice == 'Notes':
            path = 'C:/Users/KR/PycharmProjects/Automated_Note_Maker/filtered_msft_2'
        else:
            path = 'C:/Users/KR/PycharmProjects/Automated_Note_Maker/references.docx'
        #return redirect(url_for('df'), path1=path1)
    return send_file(path, as_attachment=True)

@app.route('/uploads', methods = ['GET', 'POST'])
def uploaded_file():
    if request.method=='POST':
        return redirect(url_for('downloadFile'))
    return render_template('file_upload_result.html')

if __name__ == "__main__":
    app.run( debug=True)