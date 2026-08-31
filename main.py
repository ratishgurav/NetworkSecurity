from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exceptionhandling.exception import NetworkException
from networksecurity.logging import logger
from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
from networksecurity.entity.artifactentity import DataIngestionArtifact
import sys

if __name__ == "__main__":
    try:
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        logger.logging.info("Starting data ingestion process...")
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        logger.logging.info(f"Data Ingestion Artifact: {data_ingestion_artifact}")
    except Exception as e:
        logger.logging.error(f"An error occurred during data ingestion: {e}")
        raise NetworkException(e, sys) from e
