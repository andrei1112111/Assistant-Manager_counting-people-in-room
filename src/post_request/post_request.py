import requests

from src.logger import logger


def send_post(url: str, data: dict):
    resp = requests.post(
        url,
        json=data
    )

    if resp.status_code != requests.codes.ok:
        logger.warning(f"Failed to send data to the server. Status code: {resp.status_code}")
