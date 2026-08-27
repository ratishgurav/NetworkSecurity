import os
import sys
import json
from dotenv import load_dotenv
from networksecurity.logging import logger

load_dotenv()

mongodb_url = os.getenv("MONGODB_URL_KEY")

print("MongoDB URL:", mongodb_url)

import certifi
ca = certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networksecurity.exceptionhandling.exception import NetworkException

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            logger.logging.error("An error occurred: {}".format(e))
            raise NetworkException("An error occurred in the network security module", sys)

    def csv_to_json(self, csv_file_path):
        try:
            data = pd.read_csv(csv_file_path)
            data.reset_index(drop=True, inplace=True)
            records = data.to_dict(orient="records")
            logger.logging.info(
            f"Successfully converted CSV file to JSON records: {csv_file_path}"
            )
            return records 
        except Exception as e:
            logger.logging.error("An error occurred: {}".format(e))
            raise NetworkException("An error occurred while converting CSV to JSON", sys)

    def insert_data_to_mongodb(self,records,db_name,collection_name):
        try:
            self.database = db_name
            self.collection = collection_name
            self.records = records
            self.client = pymongo.MongoClient(mongodb_url, tlsCAFile=ca)
            self.db = self.client[self.database]
            self.collection = self.db[self.collection]
            self.collection.insert_many(self.records)
            logger.logging.info(
            f"Successfully inserted {len(self.records)} records "
            f"into MongoDB collection '{collection_name}'"
            )
            return (len(self.records))
        
        except Exception as e:
            logger.logging.error("An error occurred: {}".format(e))
            raise NetworkException("An error occurred while inserting data into MongoDB", sys)

if __name__ == "__main__":
    FILE_PATH = r"Network_Data\phisingData.csv"
    DATABASE_NAME = "networksecurity"
    COLLECTION_NAME = "phishing_data"
    networkobject = NetworkDataExtract()
    records = networkobject.csv_to_json(FILE_PATH)
    print(records)
    no_of_records = networkobject.insert_data_to_mongodb(records,DATABASE_NAME, COLLECTION_NAME)
    print(f"Inserted {no_of_records} records into the MongoDB collection '{COLLECTION_NAME}' in database '{DATABASE_NAME}'.")