from apscheduler.schedulers.blocking import BlockingScheduler

from src.config import config

scheduler = BlockingScheduler()


def start_scheduler(func):
    """
    Add a cron job on every interval.minute from first_hour_time to last_hour_time in monday-friday days.
    """
    scheduler.add_job(
        func,
        'cron',
        day_of_week='mon-fri',
        timezone=config.timezone,

        hour=f"{config.scheduler_settings.first_hour_time.hour}"  # from H
             f"-"
             f"{config.scheduler_settings.last_hour_time.hour}",  # to H

        minute=f"0"
               f"-"
               f"59"
               f"/"
               f"{config.scheduler_settings.interval.minute}"  # every {} minute

    )

    scheduler.start()


def stop_scheduler():
    scheduler.shutdown()
