import os
import sys
import pandas as pd
from src.exception import CustomException
from src.util   import load_object


class PredictPipeLine:
    def __init__(self):
        pass

    def predict(self, features):
         try:
            model_path = os.path.join('artifacts', 'model.pkl')
            prepprocessor_path = os.path.join('artifacts', 'data_preprocessors.pkl')

            model = load_object(model_path)
            prepprocessor = load_object(prepprocessor_path)

            data_scale = prepprocessor.transform(features)
            prediction = model.predict(data_scale)
            
            return prediction
         except Exception as e:
                raise CustomException(e, sys)
         


class CustomerData:
    def __init__(self, description, amount):
            self.description = description
            self.amount = amount

    def get_data(self):
         try:
              input_dict = {'Description': [self.description], 'Amount': [self.amount]}
              return pd.DataFrame(input_dict)
         
         except Exception as e:
                raise CustomException(e, sys)