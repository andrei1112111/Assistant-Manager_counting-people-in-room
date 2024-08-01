import scheduler as scheduler

from logger import logger
from config import config
from post_request import send_post

import camera as camera
import detect_peoples as detect_peoples

import datetime
import base64


def run_app():
    def job():
        camera.get_camera_shot(
            config.raw_camera_shot_path
        )  # Get an Image from the camera

        peoples_inroom = detect_peoples.get_peoples_count_from_photo(
            config.raw_camera_shot_path
        )  # Get number of peoples from the Image

        if peoples_inroom == 0:
            logger.info(f"Room '{config.room_name}' is empty.")

        with open(config.raw_camera_shot_path, "rb") as f:
            im_bytes = f.read()

        im_b64 = base64.b64encode(im_bytes).decode("utf8")
        del im_bytes

        send_post(
            url=config.server.url,
            data={
                "auth_key": config.server.auth_key,
                "room": config.room_name,
                "count": peoples_inroom,
                "date": datetime.datetime.now(tz=config.timezone).strftime('%m/%d/%Y, %H:%M:%S'),
                "image": im_b64
            }
        )

        del im_b64

        logger.info(f"There are {peoples_inroom} people in the '{config.room_name}' room.")

    logger.info(f"Scheduler will work from {config.scheduler_settings.first_hour_time.strftime('%H')}:00 "
                f"to {config.scheduler_settings.last_hour_time.strftime('%H')}:00 "
                f"with interval {config.scheduler_settings.interval.strftime('%M')} minutes"
                f"!")

    job()

    scheduler.start_scheduler(job)


if __name__ == "__main__":
    run_app()
