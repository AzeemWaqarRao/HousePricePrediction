import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np 
import pandas as pd 

app = Flask(__name__)

# load model
model = pickle.load(open("model.pkl","rb"))
scaler = pickle.load(open("scaler.pkl","rb"))


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/predict',methods=['POST'])
def predict():
    pass