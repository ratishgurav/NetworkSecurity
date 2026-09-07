import yaml
from networksecurity.exceptionhandling.exception import NetworkException
from networksecurity.logging import logger
import os, sys
import numpy as np
# import dill
import pickle

def read_yaml_file(file_path: str) -> dict:
    """
    Reads a YAML file and returns its contents as a dictionary.
    
    Args:
        file_path (str): The path to the YAML file.
    """
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except Exception as e:
        raise NetworkException(e, sys) from e