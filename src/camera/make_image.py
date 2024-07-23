from . import cap
import cv2
from datetime import datetime

from PIL import Image, ImageDraw, ImageFont


def get_camera_shot(save_path):
    # for i in range(30):
    #     cap.read()
    #
    # ret, frame = cap.read()
    # cv2.imwrite(save_path, frame)

    img = Image.open("/src/tmp/test/1.png").convert("RGB")
    # img = Image.open(save_path).convert("RGB")

    img = img.resize((600, 600), Image.LANCZOS)

    draw = ImageDraw.Draw(img)

    font = ImageFont.load_default()

    draw.text((0, 0), str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')), (255, 255, 255), font=font)

    img.save(save_path, optimize=True, quality=10)
    print("Shot")
