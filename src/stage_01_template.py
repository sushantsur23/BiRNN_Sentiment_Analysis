import yaml, shutil
import argparse
import os, csv
import shutil
from tqdm import tqdm
import logging
from src.utils.common import read_yaml, create_directories
from sklearn.model_selection import train_test_split
from src.utils.Logs import Logger
import pandas as pd
import random, shutil,sys
from cc_Exception.exception import RaiseException
from statistics import mean, stdev
from sklearn import preprocessing
from sklearn.model_selection import StratifiedKFold

Logger.logg()

def main(config_path, params_path):
    ## read config files
    try:
        '''
        reading the csv file and sending it to Raw folder path
        selecting the required columns and saving it on processed folder 
        '''    
        logging.info(" ***** Stage 02 started ***** ")
        
        config = read_yaml(config_path)
        params = read_yaml(params_path)
        
        raw_data = config["data"]["raw_data"]
        
        create_directories([raw_data])

        raw_data_dir = os.path.join(raw_data)

        df = pd.read_csv("Reviews.csv", sep = ",")
        
        shutil.copyfile("Reviews.csv", os.path.join(raw_data_dir,"reviews.csv"))
        
        data_file = config["data"]["data_file"]
        
        data_file_path = os.path.join(raw_data_dir, data_file)
        
        data = pd.read_csv(data_file_path, sep = ",")
        
        data = data.drop(columns = ['Id','UserId','ProfileName','HelpfulnessNumerator','HelpfulnessDenominator','ProductId','Time'])
        
        processed_data = config["data"]["processed_data"]
        
        processed_data = os.path.join(os.getcwd(), processed_data)
        create_directories([processed_data])
        print(processed_data+'Reviews.csv')
        data.to_csv(os.path.join(processed_data,'Review.csv'), index=False)
        
        logging.info(" ***** Stage 02 ended ***** ")
    except Exception as e:
        logging.exception(e)
        raise Exception(RaiseException(e,sys)) from e
        

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="configs/config.yaml")
    args.add_argument("--params", default="params.yaml")
    parsed_args = args.parse_args()
    main(config_path=parsed_args.config, params_path=parsed_args.params)
