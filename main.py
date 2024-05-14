from src.mlProject.pipeline.stage_01_pipeline_ingestion import DataIngestionTraningPipeline
from src.mlProject import logger

STAGE_NAME = "Data ingestion stage"

try:
        logger.info(f">>>>>>>>>>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<")
        data_ingestion = DataIngestionTraningPipeline()
        data_ingestion.main()
        logger.info(f">>>>>>>>>>>>>>>>>> Stage {STAGE_NAME} completed ! <<<<<<<<<<<<<<<<<<< \n\n ===============")
except Exception as e:
        logger.exception(e)
        raise e