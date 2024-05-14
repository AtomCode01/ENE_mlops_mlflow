from src.mlProject.config.configuration import ConfigurationManger
from src.mlProject.compnents.data_ingestion import DataIngestion
from src.mlProject import logger


STAGE_NAME = "Data ingestion stage"

class DataIngestionTraningPipeline:
    def __init__(self):
        pass 

    def main(self):
        # Now comes best part. this part will hold Pipeline
            config = ConfigurationManger()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()


if __name__ == '__main__':
     try:
          logger.info(f">>>>>>>>>>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<")
          obj = DataIngestionTraningPipeline()
          obj.main()
          logger.info(f">>>>>>>>>>>>>>>>>> Stage {STAGE_NAME} completed ! <<<<<<<<<<<<<<<<<<< \n\n ===============")
     except Exception as e:
          logger.exception(e)
          raise e