import csv
import sys
import json
import requests
import time

from flask import Flask
from flask import Response

app = Flask(__name__)

@app.route('/')
def home():
    result = ""
    with requests.Session() as s:
        rdata = s.get("https://prezenta.bec.ro/europarlamentare26052019/data/pv/json/pv_AB.json")
        jdata = json.loads(rdata.content.decode('utf-8'))

        for key, value in jdata["pvs"]["temporary"]["table"]["EUP"][0].items():
            result += "\"%s\"" % key
            result += ", "
        result +="\n"

        for eup in jdata["pvs"]["temporary"]["table"]["EUP"]:
            for key, value in eup.items():
                result += "\"%s\"" % str(value)
                result += ", "
            result += "\n"
    return Response(result, mimetype='text/csv')


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
