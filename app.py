from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict', methods=['POST'])
def predict():
    data = pd.DataFrame([{
        'age': int(request.form['age']),
        'sex': request.form['sex'],
        'bmi': float(request.form['bmi']),
        'children': int(request.form['children']),
        'smoker': request.form['smoker'],
        'region': request.form['region']
    }])

    prediction = model.predict(data)[0]
    return render_template("result.html", prediction=round(prediction, 2))

if __name__ == '__main__':
    app.run(debug=True)
