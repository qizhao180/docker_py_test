from flask import Flask
from flask import Response
import time

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world, I got it"

@app.route("/healthz")
def healthz():
    resp = Response("ok")
    resp.headers['Custom-Header'] = 'Awesome'
    # this is awesome tying things
    return resp


if __name__ == "__main__":
    counter = 0
    while True:
        time.sleep(5)
        counter = counter + 1
        print("{} sleep 5 sec, wait...".format(counter))
        if (counter == 10 ):
            break

    app.run(host='0.0.0.0', port='8080')
    