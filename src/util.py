import os
import sys
from src.exception import CustomException
from src.logger import logging
import dill
from sklearn.metrics import r2_score
import pickle

def save_obj(obj, path):
    try:
        with open(path, 'wb') as f:
            dill.dump(obj, f)
    except Exception as e:
       raise CustomException(e, sys)

def evaluate(X_train, Y_train,X_test, Y_test, models):
    for model in models:
        try:
            reports ={}

            for i in range(len(models)):
                model = list(models.values())[i]
                model.fit(X_train, Y_train)
                Y_train_pred = model.predict(X_train)
                y_test_pred = model.predict(X_test)

                train_model_score = r2_score(Y_train, Y_train_pred)
                test_model_score = r2_score(Y_test, y_test_pred)

                reports[list(models.keys())[i]] = test_model_score
                
            return reports

        except Exception as e:
            raise CustomException(e, sys)               


def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)