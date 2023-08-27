from housing.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig,ModelPusherConfig,ModelEvaluationConfig,TrainingPipelineConfig
from housing.exception import HousingException
from housing.logger import logging
import sys
from housing.constant import *
from housing.util.util import read_yaml_file
class Configuration:
    def __init__(self,config_file_path:str = CONFIG_FILE_PATH,current_date_time:str=CURRENT_DATE_TIME)->None:
        try:
            self.config_info = read_yaml_file(file_path=config_file_path)
            self.training_pipeline_config=self.get_training_pipeline_config()
            self.time_stamp=CURRENT_DATE_TIME
        except Exception as e:
            raise HousingException(e,sys) from e
    def get_data_ingestion_config(self)-> DataIngestionConfig:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir  #artifact dir
            data_ingestion_artifact_dir = os.path.join(artifact_dir,DATA_INGESTION_ARTIFACT_DIR,self.time_stamp)  # artifact dir/ data_ingestion / 8262023
            data_ingestion_info = self.config_info[DATA_INGESTION_CONFIG_KEY]

            dataset_download_url = data_ingestion_info[DATA_INGESTION_DOWNLOAD_URL_KEY]
            tgz_download_dir = os.path.join( data_ingestion_artifact_dir,data_ingestion_info[DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY])
            raw_data_dir = os.path.join(data_ingestion_artifact_dir,data_ingestion_info[DATA_INGESTION_RAW_DATA_DIR_KEY])

            ingested_data_dir = os.path.join(data_ingestion_artifact_dir,data_ingestion_info[DATA_INGESTION_INGESTED_DIR_NAME_KEY])
            ingested_train_dir = os.path.join(ingested_data_dir,data_ingestion_info[DATA_INGESTION_TRAIN_DIR_KEY])
            ingested_test_dir = os.path.join(ingested_data_dir,data_ingestion_info[DATA_INGESTION_TEST_DIR_KEY])

            data_ingestion_config = DataIngestionConfig(dataset_download_url=dataset_download_url,
                tgz_download_dir=tgz_download_dir,
                raw_data_dir=raw_data_dir,
                ingested_train_dir=ingested_train_dir,
                ingested_test_dir=ingested_test_dir)
            logging.info(f"Data Ingestion Config : {data_ingestion_config}")

            return data_ingestion_config
        except Exception as e:
            raise HousingException(e, sys) from e

    def get_data_validation_config(self)-> DataValidationConfig:
        # try:
        #     schema_file_path=None
        #     get_data_validation_config=DataValidationConfig(schema_file_path=schema_file_path)
        #     return  get_data_validation_config
        pass

    def get_data_transformation_config(self)->DataTransformationConfig:
        pass

    def get_data_trainer_config(self)-> ModelTrainerConfig:
        pass

    def get_data_evaluation_config(self)->ModelEvaluationConfig:
        pass

    def get_data_pusher_config(self)-> ModelPusherConfig:
        pass

    def get_training_pipeline_config(self)->TrainingPipelineConfig:
        try:
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir = os.path.join(ROOT_DIR,training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
                                        training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY])
            training_pipeline_config= TrainingPipelineConfig(artifact_dir=artifact_dir)
            logging.info(f"Training Pipline config:{training_pipeline_config} ")
            return training_pipeline_config
        except Exception as e:
                raise HousingException(e,sys) from e