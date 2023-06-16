from flask import Flask
import pickle
from flask import *
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


app = Flask(__name__)

#import ridge regressor model and standard scaler pickle
ridge_model = pickle.load(open('Models/ridge.pkl','rb'))
Standard_Scaler = pickle.load(open('Models/scaler.pkl','rb'))

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predictdata",methods = ['GET','POST'])
def predict_datapoint():
    if request.method == 'POST':
        Temperature = float(request.form.get('Temperature'))
        Rh = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMc = float(request.form.get('FFMC'))
        DMc = float(request.form.get('DMC'))
        ISi = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        new_data_scaled = Standard_Scaler.transform([[Temperature,Rh,Ws,Rain,FFMc,DMc,ISi,Classes,Region]])
        result = ridge_model.predict(new_data_scaled)
        
        return render_template('home.html',result = result[0])
    else:
        return render_template('home.html')


if(__name__) == "__main__":
    app.run(host="0.0.0.0")