from src.mlProject.pipeline.stage_01_pipeline_ingestion import DataIngestionTraningPipeline
from src.mlProject.pipeline.stage_02_pipeline_validation import DataValidationTraningPipeline
from src.mlProject.pipeline.stage_03_pipeline_transformation import DataTransfromationTraningPipeline
from src.mlProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from src.mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline
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


STAGE_NAME = "Data validation stage"

try:
        logger.info(f">>>>>>>>>>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<")
        data_ingestion = DataValidationTraningPipeline()
        data_ingestion.main()
        logger.info(f">>>>>>>>>>>>>>>>>> Stage {STAGE_NAME} completed ! <<<<<<<<<<<<<<<<<<< \n\n ===============")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data transformation stage"

try:
        logger.info(f">>>>>>>>>>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<")
        data_ingestion = DataTransfromationTraningPipeline()
        data_ingestion.main()
        logger.info(f">>>>>>>>>>>>>>>>>> Stage {STAGE_NAME} completed ! <<<<<<<<<<<<<<<<<<< \n\n ===============")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Model trainer stage"

try:
        logger.info(f">>>>>>>>>>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<")
        data_ingestion = ModelTrainerTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>>>>>>>>>>>>>>> Stage {STAGE_NAME} completed ! <<<<<<<<<<<<<<<<<<< \n\n ===============")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Model Evaluation stage"

try:
        logger.info(f">>>>>>>>>>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<")
        data_ingestion = ModelEvaluationPipeline()
        data_ingestion.main()
        logger.info(f">>>>>>>>>>>>>>>>>> Stage {STAGE_NAME} completed ! <<<<<<<<<<<<<<<<<<< \n\n ===============")
except Exception as e:
        logger.exception(e)
        raise e