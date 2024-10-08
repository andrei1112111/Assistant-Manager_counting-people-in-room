from __future__ import annotations

from pydantic import BaseModel
import datetime
import pytz


class SchedulerSettings(BaseModel):
    interval: datetime.datetime  # like '0:15' ONLY MINUTES SUPPORTED
    first_hour_time: datetime.datetime  # like '8:30'
    last_hour_time: datetime.datetime  # like '19:00'


class ServerConfig(BaseModel):
    auth_key: str
    url: str


class ConfigModel(BaseModel):
    camera_index: int

    room_name: str

    timezone: pytz.BaseTzInfo  # like 'Asia/Novosibirsk'

    scheduler_settings: SchedulerSettings

    raw_camera_shot_path: str  # like 'src/tmp/camera_pictures/camera_image.png'

    server: ServerConfig

    class Config:  # this is necessary to allow pydantic to work with data types from other libraries
        arbitrary_types_allowed = True
