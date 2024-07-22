import requests

from src.logger import logger


def send_post(url: str, data: dict):
    print(data)
    resp = requests.post(
        url,
        json=data
    )

    if resp.status_code != requests.codes.ok:
        logger.warning("Failed to send data")
