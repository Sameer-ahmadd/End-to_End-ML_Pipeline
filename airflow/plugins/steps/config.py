import os 
from pathlib import Path 


REPO_DIR = Path(os.path.realpath(""))
INFERENCE_DATA_PATH = REPO_DIR / "data/sample_for_inference.parquet"
TRAINING_DATA_PATH = REPO_DIR / "data/hotel_bookings.parquet"

class PreprocessConfig:
    train_path = REPO_DIR / "data/preprocessed/train.parquet"
    test_path = REPO_DIR / "data/preprocessed/test.parquet"
    batch_path = REPO_DIR / "data/preprocessed/batch.parquet"


class TrainerConfig:
    model_name ="gradient-boosting"
    random_state = 42
    train_size = 0.2
    shuffle = True
    params = {
        "n_estimators": 100,
        "min_samples_split": 2,
        "min_samples_leaf": 1
    }
