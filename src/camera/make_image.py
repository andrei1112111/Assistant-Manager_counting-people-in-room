from . import cap
import cv2


def get_camera_shot(save_path):
    # for i in range(30):
    #     cap.read()
    #
    # ret, frame = cap.read()
    # cv2.imwrite(save_path, frame)

    from PIL import Image
    # Image.open("src/hash/test/2.png").convert("RGB").save(save_path)
    Image.open("src/hash/test/6.jpg").convert("RGB").save(save_path)

    print("Shot")
