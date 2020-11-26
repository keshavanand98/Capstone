from flask import Flask, render_template, request, redirect
import os
import base64
import app.TextGenerator as tg 
from flask import jsonify
# Flask config
app = Flask(__name__)
# app.secret_key = FLASK_SECRET_KEY
# app.config['WTF_CSRF_TIME_LIMIT'] = WTF_CSRF_TIME_LIMIT
UPLOAD_FOLDER_IMAGE = './static/uploads/image/'
# UPLOAD_FOLDER_CAPTION = './capstone_inner/static/uploads/caption/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

def rename_file(name):
    name,ext = os.path.splitext(name)
    return 'image'+ext

# @app.route('/')
# @app.route('/home')
# def home():
#     return render_template('index.html')
@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/image', methods=['GET','POST'])
def image():
    if request.method == 'GET':
        return render_template('index.html', result_generated = "")
    if request.method == 'POST':
        file1 = request.files['file1'] #CHAL JAYEGA
        lang =  request.form['lang'] #chal jayega
        # print(file1)
        # print(lang)
        # if(file1.filename != ""):
        file1.save(UPLOAD_FOLDER_IMAGE+rename_file(file1.filename))
        # print("*****//")
        filenameToBeSent = rename_file(file1.filename)
        # print("-----")
        # print(filenameToBeSent)
        # print("----")
        ans =tg.get_label(f'./static/uploads/image/{filenameToBeSent}',lang)
        temp=[]
        for ele in ans:
            temp.append(ele[1])
        # print(temp)

        # else:
        #     file2 = request.form['file2']
        #     imgdata = base64.b64decode(file2[22:])
        #     filenameToBeSent = "image.png"
        #     with open(UPLOAD_FOLDER_CURRENCY+"image.png", "wb") as fh:
        #         fh.write(imgdata)
        #     currency_module.get_label('./capstone_inner/static/uploads/currency/image.png'
        # )
        return jsonify(temp)
        

