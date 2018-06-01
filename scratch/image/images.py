from flask import Flask
from flask import render_template
import json
import requests
from random import randrange
#images =["./iot-img1.jpeg","./iot-img2.jpeg","./iot-img3.jpeg"]

app = Flask(__name__)








@app.route('/')
def hello():
    url='http://dserver:5001/team'
    response=requests.get(url)
    data=response.json()
    empID = randrange(0,6)
    usr=data['team'][empID]['name']
 
    return render_template('index.html',name=usr)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
