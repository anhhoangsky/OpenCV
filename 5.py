from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask import jsonify
import cv2
import sys
import os

# db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)

basedir = os.path.abspath(os.path.dirname(__file__))
# data_file = os.path.join(basedir, './')


class ScanQR(Resource):
    def get(self, file_name):
        path = basedir + "\\" + file_name + ".png"
        inputImage = cv2.imread(path)

        qrDecoder = cv2.QRCodeDetector()
        data, aasdas, asdad = qrDecoder.detectAndDecode(inputImage)
        if len(data) > 0:
            result = data
        else:
            result = "QR Code not detected"
        # conn = db_connect.connect()
        # query = conn.execute("select * from employees where EmployeeId =%s "  file_name))
        return jsonify(Decoded_Data=result)


api.add_resource(ScanQR, '/scan/<file_name>')  # Route_1


if __name__ == '__main__':
    app.run(port='5002')
