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


@app.route('/predict_api',methods=['POST'])
def predict_api():
    data = request.json['data']
    data = np.array(list(data.values())).reshape(1,-1)
    data = scaler.transform(data)
    print(data)
    result = model.predict(data)
    result = float(result[0])
    
    return jsonify(result)


@app.route('/predict',methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    data = np.array(data).reshape(1,-1)
    data = scaler.transform(data)
    output = float(model.predict(data)[0])

    return render_template("home.html",prediction_text="Predicted House Price is : "+ str(output))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)