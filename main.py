from networkSecurity.components import Data_Validation
from networkSecurity.components.Data_Ingestion import DataIngestion
from networkSecurity.components.Data_Validation import DataValidation
from networkSecurity.exception.exception import NetworkSecurityException
from networkSecurity.logging.logger import logging
from networkSecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig
from networkSecurity.entity.config_entity import TrainingPipelineConfig

import sys

if __name__=="__main__":
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")
        print(data_ingestion_artifact)
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(data_ingestion_artifact,data_validation_config)
        logging.info("Iniatiate Data validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("Data Validation completed")
        print(data_validation_artifact)
    
    except Exception as e:
        raise NetworkSecurityException(e,sys)