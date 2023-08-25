from housing.entity.config_entity import DataIngetionConfig
from housing.exception import HousingException
import sys,os
from housing.logger import logging
class DataIngestion:
    def __init__(self,data_ingestion_config: DataIngetionConfig):
        try:
            logging.info(f"{'='*20} Data Ingestion log started")
            self.data_ingestion_config=data_ingestion_config
        except Exception as e:
            raise HousingException(e,sys)

    def intiate_data_ingestion(self)-> DataIngestionArtifact:
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys) from e
