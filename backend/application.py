import time
import numpy as np
from flask import Flask, request, jsonify, flash
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
from main import FetchData
import asyncio
from tornado.platform.asyncio import AnyThreadEventLoopPolicy

asyncio.set_event_loop_policy(AnyThreadEventLoopPolicy())


application = Flask(__name__)
CORS(application)


@application.route('/get_info', methods=['POST'])
def get_info():
    package = request.get_json(force=True)
    ticker = package['text']
    data = FetchData(ticker)
    file_path = data.get_10k()
    if file_path:
        data.bolded_points(file_path)
        returned = data.sort_bold()
        # data.console_print()
        return jsonify(output=returned)
    else:
        return jsonify(output={"Error Message": "Could not download 10k"})



def printt(hello):
    print(hello)
