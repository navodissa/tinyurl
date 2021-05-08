import writeAPI as wp
from flask import Flask, request, render_template
import json

hostName = "0.0.0.0"
serverPort = 8080

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("write.html")

@app.route('/write', methods=['POST'])
def write():
    if request.method == "POST":
        record = request.form['title']
        write = wp.WriteAPI()
        result = write.writeData(record)
        return render_template('write_output.html', result=result)


@app.route('/writeAPI', methods=['POST'])
def writeAPI():
    if request.method == "POST":
        record = request.form['title']
        write = wp.WriteAPI()
        result = write.writeData(record)
        return result
        

if __name__ == '__main__':
    app.run(host=hostName, port=serverPort)
