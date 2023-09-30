import numpy as np
import pickle
from flask import Flask, render_template, request, jsonify
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

with open('MODEL.pkl', 'rb') as file:
	model = pickle.load(file)
file.close()

@app.route('/')
def Home():
    return render_template('index.html')


@app.route('/predict', methods=['POST', 'GET'])
def results():
    Type = int(request.form["Type"])
    Air_temperature_K = float(request.form["Air_temperature[K]"])
    Processtemperature_K = float(request.form["Processtemperature[K]"])
    Rotationalspeed_rpm = float(request.form["Rotationalspeed[rpm]"])
    Torque_Nm = float(request.form["Torque[Nm]"])
    Toolwear_min = float(request.form["Toolwear[min]"])
    FailureType = float(request.form["FailureType"])




    x = np.array([[Type, Air_temperature_K, Processtemperature_K, Rotationalspeed_rpm, Torque_Nm, Toolwear_min, FailureType]])
    Y_predict = model.predict(x)
    return jsonify({'Prediction': float(Y_predict)})



if __name__ == '__main__':
    app.run(debug=True, port=1010)

