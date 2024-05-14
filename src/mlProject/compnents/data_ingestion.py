import os 
import urllib.request as request  # request to download data from URL
import zipfile  # to unzip files
from src.mlProject import logger   # to take logg
from src.mlProject.utils.common import get_size
from pathlib import Path
from src.mlProject.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    #below code will donwload data and create file "DataIngestion"
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL, 
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} downloaded ! with the following info \n{headers}")
        else:
            logger.info(f"file already exists of size {get_size(Path(self.config.local_data_file))}")

    # After downloading data we also need to extract it
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)