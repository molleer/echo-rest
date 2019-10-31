import sys
import os

from flask import Flask, request, jsonify

app = Flask(__name__)

#@app.route("/", methods=['GET','POST', 'PUT', 'DELETE', 'PATCH','OPTIONS'])
@app.route("/<string:any>", methods=['GET','POST', 'PUT', 'DELETE', 'PATCH','OPTIONS'])
def home(any):
    headers = ""
    for i in request.headers.keys():
      headers+= "\t%s: %s \n" % (i, request.headers[i])
    print("Headers: \n%s" % (headers))
    print(request.json)
    print("Hello there")
    return jsonify(headers=headers, body=request.json)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=os.environ.get("LISTEN_PORT","80"))
