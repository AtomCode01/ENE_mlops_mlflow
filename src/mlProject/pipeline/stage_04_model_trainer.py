from src.mlProject.config.configuration import ConfigurationManger
from src.mlProject.compnents.model_trainer import ModelTrainer
from src.mlProject import logger
from pathlib import Path


STAGE_NAME = "Model trainer stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass 

    def main(self):
        config = ConfigurationManger()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config= ModelTrainer(config = model_trainer_config)
        model_trainer_config.train()


if __name__ == '__main__':
     try:
          logger.info(f">>>>>>>>>>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<")
          obj = ModelTrainerTrainingPipeline()
          obj.main()
          logger.info(f">>>>>>>>>>>>>>>>>> Stage {STAGE_NAME} completed ! <<<<<<<<<<<<<<<<<<< \n\n ===============")
     except Exception as e:
          logger.exception(e)
          raise e