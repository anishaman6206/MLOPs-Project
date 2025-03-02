# from src.logger import logging

# logging.debug("This is a debug message")
# logging.info("This is an info message")

from src.pipline.training_pipeline import TrainPipeline

pipline = TrainPipeline()
pipline.run_pipeline()