from .setup_camera import setup_camera

from src.config import config

cap = setup_camera(config.camera_index)

from .make_image import get_camera_shot

__all__ = [
    "get_camera_shot"
]
