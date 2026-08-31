from networksecurity.exceptionhandling.exception import NetworkException
from networksecurity.logging import logger

## Configuration for Data Ingestion

from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.artifactentity import DataIngestionArtifact

import os
import sys
import pandas as pd
import numpy as np
import pymongo
from typing import List
from sklearn.model_selection import train_test_split

from dotenv import load_dotenv
load_dotenv()

MONGODB_URL_KEY = os.getenv("MONGODB_URL_KEY")

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise NetworkException(e, sys) from e

    def export_collection_as_dataframe(self):
        """
        Read data from MongoDB collection and export it as a pandas dataframe
        """
        try:
            data_base_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name
            self.client = pymongo.MongoClient(MONGODB_URL_KEY)
            collection_name = self.client[data_base_name][collection_name]
            df = pd.DataFrame(list(collection_name.find())) ## getting the entire collection as a dataframe
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"]) 
            df.replace(to_replace="NaN", value=np.nan, inplace=True) ## replacing NaN string with np.nan
            logger.logging.info(f"Data exported from MongoDB collection: {collection_name} as DataFrame")
            return df

        except Exception as e:
            raise NetworkException(e, sys) from e

    def export_data_into_feature_store(self, df: pd.DataFrame):
        """
        Export DataFrame into feature store
        """
        try:
            feature_store_dir = self.data_ingestion_config.feature_store_dir
            os.makedirs(feature_store_dir, exist_ok=True)
            file_path = os.path.join(feature_store_dir, "feature_store.csv")
            df.to_csv(file_path, index=False, header=True)
            logger.logging.info(f"Data exported to feature store at: {file_path}")
            return df
        except Exception as e:
            raise NetworkException(e, sys) from e

    def split_data_as_train_test(self, df: pd.DataFrame):
        """
        Split DataFrame into train and test sets
        """
        try:
            train_set, test_set = train_test_split(
                df, test_size=self.data_ingestion_config.train_test_split_ratio, random_state=42
            )
            os.makedirs(self.data_ingestion_config.ingested_dir, exist_ok=True)
            train_file_path = self.data_ingestion_config.train_file_path
            test_file_path = self.data_ingestion_config.test_file_path
            train_set.to_csv(train_file_path, index=False, header=True)
            test_set.to_csv(test_file_path, index=False, header=True)
            logger.logging.info(f"Data split into train and test sets at: {train_file_path} and {test_file_path}")
            return train_file_path, test_file_path
        except Exception as e:
            raise NetworkException(e, sys) from e

    def initiate_data_ingestion(self):
        try:
            dataframe = self.export_collection_as_dataframe()
            dataframe = self.export_data_into_feature_store(dataframe)
            self.split_data_as_train_test(dataframe)
            data_ingestion_artifact = DataIngestionArtifact(
                train_file_path=self.data_ingestion_config.train_file_path,
                test_file_path=self.data_ingestion_config.test_file_path
            )
            return data_ingestion_artifact
        except Exception as e:
            raise NetworkException(e, sys) from e