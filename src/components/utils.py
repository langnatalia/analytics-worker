import logging
import os
import json
from datetime import datetime, timedelta
from typing import Dict, List

class Utils:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def load_config(self, file_path: str) -> Dict:
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            self.logger.error(f"Config file not found at {file_path}")
            return {}
        except json.JSONDecodeError as e:
            self.logger.error(f"Error parsing config file: {e}")
            return {}

    def write_json(self, data: Dict, file_path: str) -> None:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def get_current_datetime(self) -> datetime:
        return datetime.now()

    def get_time_window(self, start_time: datetime, end_time: datetime) -> List[datetime]:
        time_window = []
        current_time = start_time
        while current_time <= end_time:
            time_window.append(current_time)
            current_time += timedelta(hours=1)
        return time_window

    def create_directory(self, directory_path: str) -> None:
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

def main():
    utils = Utils()
    config = utils.load_config('config.json')
    print(config)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()