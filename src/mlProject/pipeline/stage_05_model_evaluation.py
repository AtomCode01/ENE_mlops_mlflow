from src.mlProject.config.configuration import ConfigurationManger
from src.mlProject.compnents.model_evaluation import ModelEvaluation
from src.mlProject import logger
from pathlib import Path


STAGE_NAME = "Model evaluatiion stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass 

    def main(self):
        config = ConfigurationManger()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.log_into_mlflow()

if __name__ == '__main__':
     try:
          logger.info(f">>>>>>>>>>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<")
          obj = ModelEvaluationPipeline()
          obj.main()
          logger.info(f">>>>>>>>>>>>>>>>>> Stage {STAGE_NAME} completed ! <<<<<<<<<<<<<<<<<<< \n\n ===============")
     except Exception as e:
          logger.exception(e)
          raise e