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

def parse_date(date_str: str, date_format: str = "%Y-%m-%d") -> datetime:
    try:
        return datetime.strptime(date_str, date_format)
    except ValueError:
        logger.error(f"Invalid date format: {date_str}")
        return None

def is_valid_date(date: datetime) -> bool:
    return date is not None and date <= datetime.now()

def get_time_window(start_date: datetime, end_date: datetime, window_size: int = 30) -> List:
    time_window = []
    current_date = start_date
    while current_date <= end_date:
        time_window.append(current_date)
        current_date += timedelta(days=window_size)
    return time_window

def get_env_var(var_name: str) -> str:
    return os.environ.get(var_name)

def setup_logging(log_level: str = "INFO") -> None:
    logging.basicConfig(level=getattr(logging, log_level))
    logger.info(f"Logging level set to {log_level}")