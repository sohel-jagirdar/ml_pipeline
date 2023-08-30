from collections import namedtuple
from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import logging
from housing.config.configuration import Configuration
from housing.component.data_validation import DataValidation
def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
        # logging.info("Data Ingestion Pipeline Created")
        # data_validation_config=DataValidation().get_data_transformation_config()
        # print(data_validation_config)

    except Exception as e:
        logging.error(f"{e}")
        print(e)



if __name__=="__main__":
    main()