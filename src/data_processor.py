import json
import pandas as pd
from src.logger import setup_logger

logger = setup_logger('app.log') 

def save_data_to_csv(data, file_path="output/data.csv"):
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    logger.info(f"Data extraction complete. Match data saved to {file_path}.")

def save_data_to_json(data, file_path="output/data.csv"):
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)
    logger.info(f"Data extraction complete. Match data saved to {file_path}.")