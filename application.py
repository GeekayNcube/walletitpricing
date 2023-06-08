from fastapi import FastAPI
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from  src.pipeline.predict_pipeline import *




app = FastAPI()


@app.get("/")
def root():
    return {"Hello": "World"}


@app.get("/predict{descr}/{amo}")
def predict(descr: str, amo: float):
    try:
        data = CustomerData(description=descr, amount=amo)
        predict_pipeline = PredictPipeLine()
        result = predict_pipeline.predict(data.get_data())
        results=result[0]
        return results
         
    except Exception as e:
        return {"message": "error occurred while predicting" + str(e)}


