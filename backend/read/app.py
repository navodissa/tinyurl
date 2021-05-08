import readAPI as rp
from flask import Flask
import json

hostName = "0.0.0.0"
serverPort = 8081

app = Flask(__name__)

@app.route('/read/<shorturl>', methods=['GET'])
def read(shorturl):
    read = rp.ReadAPI()
    result = read.get(shorturl)
    return (result)

 

if __name__ == '__main__':
     app.run(port=serverPort, host=hostName)