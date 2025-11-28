import sys
import os
import pandas as pd
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.utils.main_utils.utils import load_object
from networksecurity.components.model_trainer import NetworkModel
from networksecurity.constants.training_pipeline import PREPROCESSOR_SAVE_PATH,MODEL_SAVE_PATH,PREDICTION_COLUMN,PREDICTION_SAVE_PATH


class BatchPredictionPipeline:
    def __init__(self,file):
        self.file=file

    def start_prediction(self):
        try:
            df=pd.read_csv(self.file)
            preprocessor=load_object(PREPROCESSOR_SAVE_PATH)
            final_model=load_object(MODEL_SAVE_PATH)
            network_model=NetworkModel(preprocessor=preprocessor,model=final_model)
            y_pred=network_model.predict(df)
            df[PREDICTION_COLUMN]=y_pred
            df.to_csv(PREDICTION_SAVE_PATH)
            table_html=df.to_html(classes="table table-striped")
            return table_html
        except Exception as e:
            return NetworkSecurityException(e,sys)