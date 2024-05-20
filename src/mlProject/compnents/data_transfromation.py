import os
from src.mlProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from src.mlProject.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config : DataTransformationConfig):
        self.config = config


    def train_test_split(self):
        data = pd.read_csv(self.config.data_path)
        # splite data into train and test 
        train, test = train_test_split(data)
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index = False)
        
        logger.info("Splited the data into train and test")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)

