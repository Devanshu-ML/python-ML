import os

from PIL import Image
import pytesseract
from flask import app, jsonify, Flask, request
from passporteye import read_mrz
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif', '.jpeg']
app.config['UPLOAD_PATH'] = 'C:/LogFiles/CMT/data/temp'


@app.route('/api/passportEye', methods=['POST'])
def my_function():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
    passportdetails = {}
    im = Image.open("C:/Users/C58534/PycharmProjects/bookafter.jpg")
    text = pytesseract.image_to_string(im, lang='eng')
    print("text " + text)
    mrz = read_mrz(os.path.join(app.config['UPLOAD_PATH'], filename))
    mrz_data = mrz.to_dict()
    print(mrz_data)
    passportdetails["country"] = mrz_data['country']
    passportdetails["name"] = mrz_data['names']
    passportdetails["surname"] = mrz_data['surname']
    passportdetails["type"] = mrz_data['type']
    passportdetails["DOB"] = mrz_data['date_of_birth']
    passportdetails["SEX"] = mrz_data['sex']
    passportdetails["NUMBER"] = mrz_data['number']
    passportdetails["NATIONALITY"] = mrz_data['nationality']
    passportdetails["EXPIRATION DATE"] = mrz_data['expiration_date']
    # return passportdetails
    return jsonify(passportdetails)


if __name__ == '__main__':
    app.run()
