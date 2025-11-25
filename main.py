from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys

if __name__=="__main__":
    sys.dont_write_bytecode=True
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(training_pipeline_config=trainingpipelineconfig)
        dataingestion=DataIngestion(data_ingestion_config=dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact=dataingestion.initiate_data_ingestion()
        print(f"Data Ingestion Artifact {dataingestionartifact}")
        logging.info("Data Inititation Completed")
        datavalidationconfig=DataValidationConfig(training_pipeline_config=trainingpipelineconfig)
        datavalidation=DataValidation(data_ingestion_artifact=dataingestionartifact,data_validation_config=datavalidationconfig)
        logging.info("Initate the data validation")
        datavalidationartifact=datavalidation.initiate_data_validation()
        logging.info("Data Validation Completed")
        print(f"Data Validation Artifact {datavalidationartifact}")
        datatransformationconfig=DataTransformationConfig(training_pipeline_config=trainingpipelineconfig)
        datatransformation=DataTransformation(data_validation_artifact=datavalidationartifact,data_transformation_config=datatransformationconfig)
        logging.info("Data transformation started")
        datatransformationartifact=datatransformation.initiate_data_transformation()
        print(f"Data Transformation Artifact {datatransformationartifact}")
        logging.info("Data transformation completed")
    except Exception as e:
        raise NetworkSecurityException(e,sys)

