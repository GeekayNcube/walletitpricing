from fastapi import FastAPI
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler





app = FastAPI()


@app.get("/")
def root():
    return {"Hello": "World"}


@app.get("/predict{description}/{amount}")
def predict(description: str, amount: float):
    try:
        return  {"description": description, "amount": amount}
    except Exception as e:
        return {"message": "error occurred while predicting" + str(e)}


