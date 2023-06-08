import os
import sys
from src.exception import CustomException
from src.logger import logging

import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from dataclasses import dataclass
from src.util import save_obj


@dataclass
class DataTransformationConfig:
    """
    Data transformation configuration
    """
    preprocessors_obj_file_path = os.path.join('artifacts', 'data_preprocessors.pkl')



class DataTransformation:
    """
    Data transformation class
    """
    def __init__(self):
            self.data_transform_config = DataTransformationConfig()


    def get_data_transform_obj(self):
        try:
            
            numeric_columns = ['Amount']
            categorical_columns = ['Description']

            numeric_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='median')),
                    ('scaler', StandardScaler())
                ]
            )

            category_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('one_hot_encoder', OneHotEncoder()),
                    ('scaler', StandardScaler(with_mean=False))
                ]
            )

            logging.info('Category and numeric pipeline loaded')


            preprocessors = ColumnTransformer(
                [
                    ('num', numeric_pipeline, numeric_columns),
                    ('cat', category_pipeline, categorical_columns)
                ])
            
            return preprocessors

        except Exception as e:
            raise CustomException(e, sys)
     


     
    def initiate_data_transform(self, test_path:str, train_path:str):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info('Data transformation initiated')
            preprocessors = self.get_data_transform_obj()

            target_column = "CustomerAmount"
             
            logging.info('Preprocessing data')
            
            input_features_train = train_df.drop(columns=target_column, axis=1)
            target_features_train = train_df[target_column]
            logging.info(f'Train data modified')

            input_features_test = test_df.drop(columns=target_column, axis=1)
            target_features_test = test_df[target_column]

            logging.info(f'Train data modified')
          
            
            input_feature_train_arr = preprocessors.fit_transform(input_features_train)
            input_feature_test_arr = preprocessors.transform(input_features_test)


            train_arr = np.c_[input_feature_train_arr, target_features_train]
            test_arr = np.c_[input_feature_test_arr, target_features_test]

            save_obj(
                    preprocessors,self.data_transform_config.preprocessors_obj_file_path, )
            
            logging.info('Data transformation saved')

            return (train_arr, test_arr,self.data_transform_config.preprocessors_obj_file_path)

        except Exception as e:
            raise CustomException(e, sys)
     