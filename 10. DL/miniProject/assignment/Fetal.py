from flask import Flask, render_template, request 
from mysql.connector import  pooling
from base64 import b64encode
from datetime import datetime

import plotly
import plotly.express as px
import pandas as pd
import json

app = Flask( __name__ , static_folder='',template_folder='') 

@app.route("/") 
def information():
    return render_template("first.html")

@app.route("/index") 
def mainbackground():
    return render_template("index.html")

@app.route("/charts") 
def charts():
    return render_template("charts.html")

@app.route("/tables") 
def tables():
    return render_template("tables.html")

@app.route("/TensorFlow") 
def TensorFlow():
    return render_template("TensorFlow.html")

@app.route("/TensorFlow_keras") 
def TensorFlow_keras():
    return render_template("TensorFlow_keras.html")

@app.route("/Pytorch_low") 
def Pytorch_low():
    return render_template("Pytorch_low.html")

@app.route("/Pytorch_high") 
def Pytorch_high():
    return render_template("Pytorch_high.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=4000, debug = True) 