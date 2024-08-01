from . import cap
import cv2

from datetime import datetime
from pytz import timezone
from src.config import config

from src.logger import logger

from PIL import Image, ImageDraw, ImageFont

font = ImageFont.load_default()


def get_camera_shot(save_path):
    for i in range(30):
        cap.read()

    ret, frame = cap.read()
    cv2.imwrite(save_path, frame)

    del ret, frame

    # img = Image.open("/src/tmp/test/1.png").convert("RGB")
    img = Image.open(save_path).convert("RGB")

    img = img.resize((600, 600), Image.LANCZOS)

    draw = ImageDraw.Draw(img)

    draw.text(
        (0, 0),
        str(datetime.now(tz=timezone(str(config.timezone))).strftime('%Y-%m-%d %H:%M:%S')),
        (255, 255, 255), font=font
    )

    del draw, img

    logger.info("Camera shot!")
