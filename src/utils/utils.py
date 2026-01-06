import logging
import os
import json
from datetime import datetime, timedelta
from typing import Dict, List

logger = logging.getLogger(__name__)

def load_config(file_path: str) -> Dict:
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        logger.error(f"Config file not found: {file_path}")
        return {}
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse config file: {e}")
        return {}

def save_config(file_path: str, config: Dict) -> None:
    try:
        with open(file_path, 'w') as file:
            json.dump(config, file, indent=4)
    except Exception as e:
        logger.error(f"Failed to save config file: {e}")

def get_current_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_time_diff(start_time: str, end_time: str) -> timedelta:
    start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_time = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    return end_time - start_time

def is_file_exists(file_path: str) -> bool:
    return os.path.isfile(file_path)

def get_file_size(file_path: str) -> int:
    if is_file_exists(file_path):
        return os.path.getsize(file_path)
    else:
        return 0

def get_file_extension(file_path: str) -> str:
    return os.path.splitext(file_path)[1]

def split_list(input_list: List, chunk_size: int) -> List:
    return [input_list[i:i + chunk_size] for i in range(0, len(input_list), chunk_size)]