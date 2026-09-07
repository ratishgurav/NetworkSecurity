from datetime import datetime
import os
from networksecurity.constants import training_pipeline as tp

print(tp.PIPELINE_NAME)
print(tp.ARTIFACTS_DIR)

class TrainingPipelineConfig:
    def __init__(self, timestamp=datetime.now()):
        self.pipeline_name = tp.PIPELINE_NAME
        self.artifacts_dir = tp.ARTIFACTS_DIR
        self.timestamp: str = timestamp.strftime("%m%d%Y__%H%M%S")
        self.artifacts_dir = os.path.join(
            self.artifacts_dir, self.timestamp
        )

class DataIngestionConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.database_name = tp.DATA_INGESTION_DATABASE_NAME
        self.collection_name = tp.DATA_INGESTION_COLLECTION_NAME
        self.data_ingestion_dir = os.path.join(
            training_pipeline_config.artifacts_dir, tp.DATA_INGESTION_DIR_NAME
        )
        self.feature_store_dir = os.path.join(
            self.data_ingestion_dir, tp.DATA_INGESTION_FEATURE_STORE_DIR
        )
        self.ingested_dir = os.path.join(
            self.data_ingestion_dir, tp.DATA_INGESTION_INGESTED_DIR
        )
        self.train_file_path = os.path.join(
            self.ingested_dir, tp.TRAIN_FILE_NAME
        )
        self.test_file_path = os.path.join(
            self.ingested_dir, tp.TEST_FILE_NAME
        )
        self.train_test_split_ratio = tp.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        self.collection_name = tp.DATA_INGESTION_COLLECTION_NAME
        self.database_name = tp.DATA_INGESTION_DATABASE_NAME

class DataValidationConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.data_validation_dir = os.path.join(
            training_pipeline_config.artifacts_dir, tp.DATA_VALIDATION_DIR_NAME
        )
        self.valid_data_dir = os.path.join(
            self.data_validation_dir, tp.DATA_VALIDATION_VALID_DIR
        )
        self.invalid_data_dir = os.path.join(
            self.data_validation_dir, tp.DATA_VALIDATION_INVALID_DIR
        )
        self.valid_train_file_path = os.path.join(
            self.valid_data_dir, tp.TRAIN_FILE_NAME
        )
        self.valid_test_file_path = os.path.join(
            self.valid_data_dir, tp.TEST_FILE_NAME
        )
        self.invalid_train_file_path = os.path.join(
            self.invalid_data_dir, tp.TRAIN_FILE_NAME
        )
        self.invalid_test_file_path = os.path.join(
            self.invalid_data_dir, tp.TEST_FILE_NAME
        )
        self.drift_report_dir = os.path.join(
            self.data_validation_dir, tp.DATA_VALIDATION_DRIFT_REPORT_DIR
        )
        self.drift_report_file_path = os.path.join(
            self.drift_report_dir, tp.DATA_VALIDATION_DRIFT_REPORT_FILE_NAME
        )