"""
Fetching the data from passed url
"""

import requests
from utils.logger import logger


@logger
def hit_url(url):
    """

    Args: Fetches the data of one of the url from `swapi.dev`
        url: https://swapi.dev/api/{resource}/{resource_id}/

    Returns: Response of the url in int data type

    """
    response_ = requests.get(url)
    if response_.status_code != 200:
        response_.raise_for_status()
    else:
        return response_
