from dotenv import load_dotenv
import pytz
import os
import datetime

from .config_models import ConfigModel


def load_config() -> ConfigModel:
    load_dotenv()  # load variables from .env

    config_data: dict = {
        "camera_index": os.getenv("CAMERA_INDEX"),
        "room_name": os.getenv("ROOM_NAME"),
        "timezone": pytz.timezone(os.getenv("TIMEZONE")),
        "scheduler_settings": {
            "interval": datetime.datetime.strptime(os.getenv("SCHEDULER_INTERVAL_MINUTE"), "%M"),
            "first_hour_time": datetime.datetime.strptime(os.getenv("SCHEDULER_FIRST_HOUR"), "%H"),
            "last_hour_time": datetime.datetime.strptime(os.getenv("SCHEDULER_LAST_HOUR"), "%H"),
        },
        "raw_camera_shot_path": os.getenv("RAW_CAMERA_SHOT_PATH"),
        "server": {
            "auth_key": os.getenv("RESTAPI_AUTH_KEY"),
            "url": os.getenv("SERVER_URL"),
        },
    }

    # Validate config
    config_model = ConfigModel(**config_data)

    del config_data

    return config_model  # config successfully loaded
