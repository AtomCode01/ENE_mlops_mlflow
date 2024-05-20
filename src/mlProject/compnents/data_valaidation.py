import os 
import pandas as pd
from src.mlProject import logger
from src.mlProject.entity.config_entity import DataValidationConfig



class DataValidation:
    def __init__(self, config : DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        validation_status = None

        data = pd.read_csv(self.config.unzip_data_file)
        all_cols = list(data.columns)

        all_schema = self.config.all_shecma.keys()

        for cols in all_cols:
            if cols not in all_cols:
                validation_status = False
                with open(self.config.STATUS_FILE, 'w') as f:
                    f.write(f"Validation status: {validation_status}")
            else:
                validation_status = True
                with open(self.config.STATUS_FILE, 'w') as f:
                    f.write(f"Validation status: {validation_status}")
        return validation_status
        