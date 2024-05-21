from dataclasses import dataclass
from pathlib import Path
# this is not python class but dataclass. it not use "self"

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen= True)
class DataValidationConfig:
    root_dir : Path
    STATUS_FILE : str
    unzip_data_file : Path
    all_shecma : dict


@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path


@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir : Path
    test_data_path : Path
    train_data_path : Path
    model_name : str
    alpha : float       #---------- from params.yaml
    l1_ratio : float    #--------|
    target_column : str #========== from schema.yaml


@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    all_params: dict
    metric_file_name: Path
    target_column: str
    mlflow_uri: str