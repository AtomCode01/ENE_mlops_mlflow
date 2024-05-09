import os
from box.exceptions import BoxValueError
import yaml
from mlProject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
 
@ensure_annotations 
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """ 
    Read yaml files and return 
    
    Args: 
        path_to_yaml : (str) pth of yaml files
    Raise:
        ValueError if file path is empty
    Return:
        ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file :{path_to_yaml} is loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, varbose= True):
    """
        Create the list of directories
        Args:
            path_to_directories (list): list of the path of directories
            ignore_log (bool, optional): ignores if multiple dirs to be created at same time. default is False
    """

    for path in (path_to_directories):
        os.makedirs(path, exist_ok=True)
        if varbose:
            logger.info(f"created directories at {path}")

@ensure_annotations
def save_json(path: Path, data: dict):

    with open(path, "w") as f:
        """" 
        Save file in json
        Args:
            path: path to the json
            dict: The data will be saved on json file
        """
        json.dump(data, f, indent=4)
        
@ensure_annotations
def load_json(path: Path)-> ConfigBox:
    """"
    load to json files
    Args:
        path: path to json file
    Return:
        ConfigBox: data in class atribute instead to dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.inof(f"json file loaded successfully form : {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(path: Path, data: Any):
    """
    Saves binary files
    Args: 
        path (path): path to binary file
        data (Any): it will save any python object in binary format
    """
    joblib.dump(value=Any, filename= path)
    logger.info(f"binary file saved at {path}")

@ensure_annotations
def load_bin(path: Path)-> Any:
    """
    load binary file
    Args:
        path (Path): path to binary file
    Return:
        Any: load all data from binary file
    """

    data = joblib.load(path)
    logger.info(f"binary file load from: {path}")
    return data

def get_size(path: Path)-> str:
    """
    Gives file size in KB
    Args: 
        path: path of file
    Return:
        give the size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"
