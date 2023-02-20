import json
from flask import Flask
from flask import request, Response

from common import *


app = Flask(__name__)
BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))
RESOURCE_FOLDER = os.path.join(BASE_FOLDER, "resources")

@app.route('/')
def hello_world():
    with open(os.path.join(RESOURCE_FOLDER, "response.json")) as f:
        return json.loads(f.read())


def test_str():
    send_data = ""
    _name = f"===> {platform.node()}  <===\n"
    send_data += _name + "test_send!!!!!!!\n" + "--->test send<---"
    return send_data


@app.route('/send_data', methods=['GET', 'POST'])
def send_data2telegram():
    """Пересылаем переданное сообщение в переданный канал"""
    channel = request.args.get('channel', type=str)
    send_data = request.args.get('send', type=str)
    if channel == "doctors":
        send_doctors(send_data)
    elif channel == "stat":
        send_statistics(send_data)
    else:
        raise ValueError(f"Incorrect value {channel}")
    return send_data

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)