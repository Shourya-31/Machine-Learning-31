import pickle
from flask import Flask,request,jsonify,render_template
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app=application

@app.route("/")
def index():
    return "Hello, World!"

if __name__=="__main__":
    app.run(host="0.0.0.0")