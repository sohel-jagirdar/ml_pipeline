from housing.constant import *
from housing.util.util import read_yaml_file
import pandas as pd

import os,sys

CONFIG_DIR = "config"
CONFIG_FILE_NAME = "config.yaml"

# data=read_yaml_file(CONFIG_FILE_PATH)
# artifact=data[TRAINING_PIPELINE_CONFIG_KEY][TRAINING_PIPELINE_ARTIFACT_DIR_KEY]
# train_data_folder=data[DATA_INGESTION_CONFIG_KEY][DATA_INGESTION_TRAIN_DIR_KEY]
# train_data_folder

train_file = os.path.join(ROOT_DIR,"housing",'artifact','data_ingestion','2023-08-27-15-40-58','ingested_data','train','housing.csv')



# print(os.listdir(CONFIG_FILE_PATH))

print(train_file)

df=pd.read_csv(train_file)

print(df.head())

