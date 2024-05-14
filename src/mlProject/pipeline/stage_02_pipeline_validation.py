from src.mlProject.config.configuration import ConfigurationManger
from src.mlProject.compnents.data_valaidation import DataValidation
from src.mlProject import logger


STAGE_NAME = "Data validation stage"

class DataValidationTraningPipeline:
    def __init__(self):
        pass 

    def main(self):
        # Now comes best part. this part will hold Pipeline
            config = ConfigurationManger()      # setup files
            data_validation_config = config.get_validation_config()
            data_validation = DataValidation(config = data_validation_config)
            data_validation.validate_all_columns()


if __name__ == '__main__':
     try:
          logger.info(f">>>>>>>>>>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<")
          obj = DataValidationTraningPipeline()
          obj.main()
          logger.info(f">>>>>>>>>>>>>>>>>> Stage {STAGE_NAME} completed ! <<<<<<<<<<<<<<<<<<< \n\n ===============")
     except Exception as e:
          logger.exception(e)
          raise e