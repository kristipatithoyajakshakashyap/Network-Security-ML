import os
import sys
import json
from dotenv import load_dotenv
load_dotenv()
from pymongo.mongo_client import MongoClient
import certifi
import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecuirtyException
from networksecurity.logging.logger import logging

MONGO_DB_URL=os.getenv("MONGO_DB_URL")
ca=certifi.where()


class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecuirtyException(e,sys)

    def cv_to_json_convertor(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecuirtyException(e,sys)

    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records
            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            self.databasae=self.mongo_client[self.database]
            self.collection=self.databasae[self.collection]
            self.collection.insert_many(self.records)
            return (len(self.records))
        except Exception as e:
            raise NetworkSecuirtyException(e,sys)

if __name__=="__main__":
    FILE_PATH="Network_Data\phisingData.csv"
    DATABASE="KASHYAPAI"
    Collection="NetworkData"
    networkobj=NetworkDataExtract()
    records=networkobj.cv_to_json_convertor(file_path=FILE_PATH)
    print(records)
    no_of_records=networkobj.insert_data_mongodb(records,DATABASE,Collection)
    print(no_of_records)