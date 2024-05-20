from src.mlProject.config.configuration import ConfigurationManger
from src.mlProject.compnents.data_transfromation import DataTransformation
from src.mlProject import logger
from pathlib import Path


STAGE_NAME = "Data transformation stage"

class DataTransfromationTraningPipeline:
    def __init__(self):
        pass 

    def main(self):
        # Now comes best part. this part will hold Pipeline
        try:
            with open(Path("artifacts/data_validation/status.txt"), 'r') as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                config = ConfigurationManger()
                data_transformation_config = config.get_data_trainsfromation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_split()
            else:
                raise Exception("Your data seems not valid")
        except Exception as e:
            raise e

if __name__ == '__main__':
     try:
          logger.info(f">>>>>>>>>>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<")
          obj = DataTransfromationTraningPipeline()
          obj.main()
          logger.info(f">>>>>>>>>>>>>>>>>> Stage {STAGE_NAME} completed ! <<<<<<<<<<<<<<<<<<< \n\n ===============")
     except Exception as e:
          logger.exception(e)
          raise e