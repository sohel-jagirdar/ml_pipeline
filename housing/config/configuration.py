from housing.entity.config_entity import DataIngetionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig,ModelPusherConfig,ModelEvaluationConfig,TrainingPipelineConfig
from housing.exception import HousingException
from housing.logger import logging
import sys
from housing.constant import *

class Configuration:
    def __init__(self,config_file_path:str = CONFIG_FILE_PATH,current_date_time:str=CURRENT_DATE_TIME)->None:
        self.config_info = read_yaml_file(file_path=config_file_path)
        self.training_pipeline_config=self.get_data_traning_pipline_config()
        self.time_stamp=CURRENT_DATE_TIME


    def get_data_ingestion_config(self)-> DataIngetionConfig:
        pass

    def get_data_validation_config(self)-> DataValidationConfig:
        pass

    def get_data_tranformation_config(self)->DataTransformationConfig:
        pass

    def get_data_trainer_config(self)-> ModelTrainerConfig:
        pass

    def get_data_evaluation_config(self)->ModelEvaluationConfig:
        pass

    def get_data_pusher_config(self)-> ModelPusherConfig:
        pass

    def get_data_traning_pipline_config(self)->TrainingPipelineConfig:
        try:
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir = os.path.join(ROOT_DIR,
                                  training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
                                        training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY])
            training_pipeline_config= TrainingPipelineConfig(artifact_dir=artifact_dir)
            logging.info(f"Training Pipline config:{training_pipeline_config} ")
            return training_pipeline_config
        except Exception as e:
                raise HousingException(e,sys) from e