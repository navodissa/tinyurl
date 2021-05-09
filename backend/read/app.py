import readAPI as rp
from flask import Flask, request, render_template
import json

hostName = "0.0.0.0"
serverPort = 8081

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("read.html")


@app.route('/read', methods=['GET'])
def read():
    if request.method == "GET":
        record = request.args.get('title')
        read = rp.ReadAPI()
        result = read.readData(record)
        return render_template('read_output.html', result=result)
 

@app.route('/readAPI', methods=['GET'])
def readAPI():
    if request.method == "GET":
        record = request.form['title']
        read = rp.ReadAPI()
        result = read.readAPI(record)
        return (result)


if __name__ == '__main__':
     app.run(port=serverPort, host=hostName)