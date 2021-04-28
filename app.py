# 1. Library imports
import uvicorn
from fastapi import FastAPI
from Hearts import Heart
import numpy as np
import pickle
import pandas as pd


app = FastAPI()
pickle_in = open("./model/heart-dieases.pickle","rb")
classifier=pickle.load(pickle_in)

@app.post('/predict')
def predictHeartDieases(data:Heart):
    data = data.dict()
    age=data['age']
    sex=data['sex']
    cp=data['cp']
    trestbps=data['trestbps']
    chol=data['chol']
    fbs=data['fbs']
    restecg=data['restecg']
    thalach=data['thalach']
    exang=data['exang']
    oldpeak=data['oldpeak']
    slope=data['slope']
    ca=data['ca']
    thal=data['thal']

    prediction = classifier.predict([[
    	age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
    
    if(prediction[0] != 0):
        return {"status" : "Dieasesed"}
    else:
        return {"status" : "Not Dieasesed"}
    
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)