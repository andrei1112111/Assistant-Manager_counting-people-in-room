import src.scheduler as scheduler
from src.logger import logger
from src.config import config

import src.camera as camera
import src.detect_peoples as detect_peoples


def run_app():
    def job():
        camera.get_camera_shot(
            config.raw_camera_shot_path
        )  # Get an Image from the camera

        peoples_inroom = detect_peoples.get_peoples_count_from_photo(
            config.raw_camera_shot_path,
            config.bounded_camera_shot_path
        )  # Get number of peoples from the Image

        # send number to <--.-->
        logger.info(f"There are {peoples_inroom} people in the '{config.room_name}' room.")
        #

    job()

    logger.info(f"Scheduler will work from {config.scheduler_settings.first_hour_time.strftime('%H')}:00 "
                f"to {config.scheduler_settings.last_hour_time.strftime('%H')}:00 "
                f"with interval {config.scheduler_settings.interval.strftime('%M')} minutes"
                f"!")

    scheduler.start_scheduler(job)


if __name__ == "__main__":
    run_app()
