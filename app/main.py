from flask import Flask,request,Response
import requests
import json

app = Flask(__name__)


@app.route("/codetostate")
def getstate():
    code = request.args.get('code')
    url = "http://data-service-clusterip.default.svc.cluster.local/codes"
    response = requests.get(url)
    data = json.loads(response.text)
    result = data[code.upper()]
    return result, 200


@app.route("/statetocode")
def getcode():
    state = request.args.get('state')
    url = "http://data-service-clusterip.default.svc.cluster.local/states"
    response = requests.get(url)
    data = json.loads(response.text)
    result = data[state.lower()]
    return json.dumps(result), 200


@app.route("/")
def welcome():
    return Response("Welcome to 111111", status=200)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
