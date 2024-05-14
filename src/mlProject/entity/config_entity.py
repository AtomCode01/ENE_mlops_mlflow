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