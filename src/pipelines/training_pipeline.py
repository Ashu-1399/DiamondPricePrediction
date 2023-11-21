import os, sys
# sys.path.append("..")

from src.logger import logging
from src.exception import CustomException
import pandas as pd
from src.components import DataIngestion

if __name__ == "__main__":
    obj = DataIngestion()
    train_data_path, test_data_path = obj.initiate_data_ingestion
    print(train_data_path,test_data_path)