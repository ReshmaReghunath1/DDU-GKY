import numpy as np
import pickle
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

with open('MODEL.pkl', 'rb') as file:
	model = pickle.load(file)
file.close()


@app.route('/')
def Home():
    return render_template('index.html')


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    Age = float(request.form["Age"])
    YearsofExperience = float(request.form["YearsofExperience"])

    x = np.array([[Age, YearsofExperience]])
    Y_predict = model.predict(x)
    return jsonify({'Prediction': float(Y_predict)})



if __name__ == '__main__':
    app.run(debug=True, port=1010)

