from flask import Flask, render_template
from urllib import request
import datetime
import random
import os

app = Flask(__name__)

@app.route('/')
def attack():
    targreq=request.Request(os.getenv('TARGET_URL'))
    for i in range(int(os.getenv('NUM_REQUESTS'))):
        response=request.urlopen(targreq)
        #print(response)
    return render_template('index.html')

if __name__=="__main__":
    app.run()
