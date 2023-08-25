from collections import nametuple

DataIngetionConfig = namedtuple("DataIngetionConfig",['dataset_download_url','tgz_download_dir','raw_data_dir','ingested_train_dir','ingested_test_dir'])



DataValidationConfig=nametuple("DataValidationConfig" , ["schema_file_path"])


DataTransformationConfig = nametuple("DataTransformationConfig",["add_bedroom_per_room",
                                                                 "transformed_train_dir",
                                                                 "transformed_test_dir",
                                                                 "preprocessed_object_file_path"])


ModelTrainerConfig=nametuple("ModelTrainerConfig",["trained_model_file_path","base_accuracy"])


ModelEvaluationConfig=nametuple("ModelEvaluationConfig",["model_evaluation_file_path","time_stamp"])


ModelPusherConfig=nametuple("ModelPusherConfig",["export_dir_path"])


