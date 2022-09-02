import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np 
import pandas as pd 
import numpy as np

app = Flask(__name__)

# load model
model = pickle.load(open("model.pkl","rb"))
scaler = pickle.load(open("scaler.pkl","rb"))


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/predict',methods=['POST'])
def predict():
    data = request.json['data']
    data = np.array(list(data.values())).reshape(1,-1)
    data = scaler.transform(data)
    print(data)
    result = model.predict(data)
    result = float(result[0])
    
    return jsonify(result)


if __name__ == "__main__":
    app.run()