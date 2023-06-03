import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

@dataclass
class DataInjectionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'raw.csv')
 


class DataInjection:
    def __init__(self):
        self.config = DataInjectionConfig()

    def inject_data(self):
        logging.info('Injecting data')
        try:
            data = pd.read_csv("data/data.csv")

            os.makedirs(os.path.dirname(self.config.train_data_path), exist_ok=True)

            data.to_csv(self.config.raw_data_path, index=False,header=True)
            
            train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

            train_data.to_csv(self.config.train_data_path, index=False, header=True)
            test_data.to_csv(self.config.test_data_path, index=False, header=True)
            
            logging.info('Data injected successfully')

            return (
                 self.config.train_data_path,
                 self.config.test_data_path
            )

        except Exception as e:
                raise CustomException(e, sys)
        

if __name__ == '__main__':
    data_injection = DataInjection()
    train_data, test_data = data_injection.inject_data()

    data_transformation = DataTransformation()
    data_transformation.initiate_data_transform(train_data, test_data)




