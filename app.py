from flask import Flask
from flask import json
import logging

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

app = Flask(__name__)

@app.route('/status')
def status():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )
    logging.debug("my page is coming")
    return response

@app.route('/metrics')
def metrics():
    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )
    logging.debug("my page is coming")
    return response

@app.route("/")
def hello():
    logging.info("my page is coming")
    logging.debug("my page is coming")
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, use_debugger=True,)