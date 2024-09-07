# ML Pipeline using AWS and Airflow: https://aws.amazon.com/fr/blogs/machine-learning/build-end-to-end-machine-learning-workflows-with-amazon-sagemaker-and-apache-airflow/
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
import sys
sys.path.append('../../plugins/steps')

from steps.preprocess_step import PreprocessStep
from steps.utils.data_classes import PreprocessingData
from steps.config import (
    TRAINING_DATA_PATH,
    TrainerConfig,
    PreprocessConfig,
)

# Preparation
inference_mode = False
preprocessing_data = PreprocessingData(
    train_path=PreprocessConfig.train_path,
    test_path=PreprocessConfig.test_path
)

# Steps
preprocess_step = PreprocessStep(
    inference_mode=inference_mode, 
    preprocessing_data=preprocessing_data
)

default_args = {
    "owner": "user",                     # user's name
    "depends_on_past": False,            # keeps a task from getting triggered if the previous schedule for the task hasn’t succeeded.
    "retries": 0,                        # Number of retries for a dag 
    "catchup": False,                    # Run the dag from the start_date to today in respect to the trigger frequency 
}

with DAG(
    "training-pipeline",                 # Dag name
    default_args=default_args,           # Default dag's arguments that can be share accross dags 
    start_date=datetime(2023, 12, 19),   # Reference date for the scheduler (mandatory)
    tags=["training"],                   # tags
    schedule=None,                       # No repetition
) as dag:
    preprocessing_task = PythonOperator(
        task_id="preprocessing",
        python_callable=preprocess_step,
        op_kwargs={"data_path": TRAINING_DATA_PATH},
    )
    
    preprocessing_task