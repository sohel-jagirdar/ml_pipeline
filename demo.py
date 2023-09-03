from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import logging
from housing.config.configuration import Configuartion
from housing.component.data_transformation import DataTransformation
import os
def main():
    try:
        config_path = os.path.join("config","config.yaml")
        pipeline = Pipeline(Configuartion(config_file_path=config_path))
        #pipeline.run_pipeline()
        pipeline.start()
        logging.info("main function execution completed.")
        # # data_validation_config = Configuartion().get_data_transformation_config()
        # # print(data_validation_config)
        # schema_file_path=r"D:\Project\machine_learning_project\config\schema.yaml"
        # file_path=r"D:\Project\machine_learning_project\housing\artifact\data_ingestion\2022-06-27-19-13-17\ingested_data\train\housing.csv"

        # df= DataTransformation.load_data(file_path=file_path,schema_file_path=schema_file_path)
        # print(df.columns)
        # print(df.dtypes)

    except Exception as e:
        logging.error(f"{e}")
        print(e)



if __name__=="__main__":
    main()



# from threading import Thread
# import time
# class DemoThread(Thread):
#     def __init__(self,*args,**kwargs):
#         super().__init__(daemon=False,name="demo_thread")
#
#     def print_msg(self):
#         time.sleep(5)
#         print("I was called by thread ")
#
#     def run(self):
#         self.print_msg()
#
# a=DemoThread()
#
# print("Im Waiting for print massage to complete") # Immidiate response to user
# a.start()
# a.join() # run process smoother or connect thread in one flow



# from collections import namedtuple
# Experiment = namedtuple("Experiment", ["experiment_id", "initialization_timestamp", "artifact_time_stamp",
#                                        "running_status", "start_time", "stop_time", "execution_time", "message",
#                                        "experiment_file_path", "accuracy", "is_model_accepted"])
#
# Experiment(*([None] * 11))
# print(Experiment["experiment_id"])

