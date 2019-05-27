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
    result += download("AB")
    result += download("SR")
    return Response(result, mimetype='text/csv')

def download(county):
    result = ""
    with requests.Session() as s:
        rdata = s.get("https://prezenta.bec.ro/europarlamentare26052019/data/pv/json/pv_%s.json" % county)
        jdata = json.loads(rdata.content.decode('utf-8'))

        if county == "AB":
            for key, value in jdata["pvs"]["temporary"]["table"]["EUP"][0].items():
                result += "\"%s\"" % key
                result += ", "
            result +="\n"

        for eup in jdata["pvs"]["temporary"]["table"]["EUP"]:
            for key, value in eup.items():
                result += "\"%s\"" % str(value)
                result += ", "
            result += "\n"
        return result

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
