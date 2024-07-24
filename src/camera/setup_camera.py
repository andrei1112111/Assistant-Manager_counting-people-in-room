from cv2 import VideoCapture


def setup_camera(camera_index):
    return VideoCapture(camera_index)
