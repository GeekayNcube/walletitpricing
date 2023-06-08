import os
import sys
from dataclasses import dataclass
'''from catboost import CatBostRegressor'''
from sklearn.ensemble import (AdaBoostRegressor, GradientBoostingRegressor, RandomForestRegressor)
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import r2_score

from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
'''from xgboost import XGBRegressor'''


from src.exception import CustomException
from src.logger import logging
from src.util import (
    evaluate,
    save_obj
)


@dataclass
class ModelTrainerConfig:
    train_model_file_path =os.path.join("artifacts", "model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()



    def train_model(self, train_array, test_array):
        try:
            logging.info("preprocessing data")
       

            x_train, y_train, x_test, y_test = (train_array[:,:-1], train_array[:,-1],  test_array[:,:-1], test_array[:,-1])

            models ={
                "RandomForestRegressor": RandomForestRegressor(),
                "DecisionTreeRegressor": DecisionTreeRegressor(),
                "GradientBoostingRegressor": GradientBoostingRegressor(),
                "LinearRegression": LogisticRegression(),
                "K-neighborsRegressor": KNeighborsRegressor(),
                "AdaBoostRegressor": AdaBoostRegressor(),
                "LogisticRegression": LogisticRegression(),
            }

            model_report:dict = evaluate(x_train, y_train, x_test, y_test, models)

            best_model_score = max(sorted(model_report.values()))

            logging.info(f"best model score: {best_model_score}")

            best_model_name = list(model_report.keys())[
                                                            list(model_report.values()).index(best_model_score)
                                                        ]
            
            logging.info(f"best model name: {best_model_name}")

            model = models[best_model_name]


            if best_model_score < 0.6:
                raise CustomException(f"No model found with best score")
            
            save_obj(model, self.model_trainer_config.train_model_file_path)

            predected = model.predict(x_test)

            r2_square = r2_score(y_test, predected)

            return r2_square
            

        except Exception as e:
            raise CustomException(e,sys)





