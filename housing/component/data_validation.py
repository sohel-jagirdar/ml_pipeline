import os,sys
from housing.logger import logging
from housing.exception import HousingException
from housing.entity.config_entity import DataValidationConfig
from housing.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
from housing.component.data_ingestion import DataIngestion
from housing.util.util import read_yaml_file
import pandas as pd
import numpy as np
from evidently.model import Profile
from evidently.model_profile.sections import DataDriftProfileSection
from evidently.dashboard import Dashboard
from evidently.dashboard.tabs import DataDriftTab

class DataValidation:
    def __init__(self,data_validation_config:DataValidationConfig,data_ingestion_artifact:DataIngestionArtifact,config:DataIngestion):
        try:
            self.data_validation_config= data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact
        except Exception as e:
            raise HousingException(e,sys)

    def is_train_test_file_exist(self)->bool:
        try:
            logging.imfo("Checking if training file available")
            is_train_file_exist = False
            is_test_file_exist=False

            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            is_train_file_exist=os.path.exist(train_file_path)
            is_test_file_exist = os.path.exist(test_file_path)
            is_available = is_test_file_exist and is_train_file_exist

            logging.imfo(f"Is training file exist ? {is_available} ")
            if not is_available:
                raise HousingException("Training or Testing file is not available")
            return is_available
        except Exception as e:
            raise HousingException(e, sys) from e


    def validate_dataset_schema(self):
        try:
            validate_status= False

            train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)
            validate_status=True

        except Exception as e:
            raise HousingException(e,sys) from e

    def get_train_test_df(self):
        try:
            validate_status = False

            train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)
            return train_df,test_df

        except Exception as e:
            raise HousingException(e, sys) from e

    def get_and_save_data_drift_report(self):
        try:
            profile=Profile(sections=[DataDriftProfileSection()])
            train_df,test_df= self.get_train_test_df()
            profile.calculate(train_df,test_df)
            report=json.loads(profile.json())

            report_file_path=self.data_validation_config.report_file_path
            report_dir=os.path.dirname(report_file_path)

            os.makedirs(report_dir,exist_ok=True)

            with open(report_file_path,"w") as report_file:
                json.dump(report,report_file,indent=6)

            return report

        except Exception as e:
            raise HousingException(e,sys) from e

    def deduct_outliers(self):
        pass

    def save_data_drift_report(self):
        try:
            dashboard=Dashboard(tabs=[DataDriftTab()])
            train_df, test_df = self.get_train_test_df()
            dashboad.calculate(train_df,test_df)

            report_page_file_path = self.data_validation_config.report_file_path
            report_page_dir = os.path.dirname(report_file_path)

            os.makedirs(report_page_dir, exist_ok=True)
            dashboard.save(report_page_file_path)


        except Exception as e:
            raise HousingException(e,sys) from e



    def is_data_drift_found(self):
        try:
            report=self.get_data_and_save_data_drift_report()
            self.save_data_drift_report_page()
            return True
        except Exception as e:
            raise HousingException(e,sys) from e
    def initiate_data_validation(self)-> DataValidationArtifact:
        try:
             self.is_train_test_file_exist()
             self.validate_dataset_schema()
             self.is_data_drift_found()
             data_validatation_artifact=DataValidationArtifact(
                 schema_file_path=self.data_validation_config.schema_file_path,
                 report_file_path=self.data_validation_config.report_file_path,
                 report_page_file_path=self.data_validation_config.report_page_file_path,
                 is_validated=True,
                 massage=" Data Validation Performed Successfully "
             )

             logging.info(f" Data Validation Artifact : {data_validatation_artifact}")

        except Exception as e:
            raise HousingException(e, sys) from e