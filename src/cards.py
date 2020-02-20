import json
import os
from collections import defaultdict
from typing import Dict

from data.api_magic_client import MagicTheGatheringAPIClient


def __get_cards(
        url: str = None,
        path: str = None,
) -> Dict:
    """
    Get all cards from Magic The Gathering API.

    :param str url: URL
    :param str path: path of the local file
    :return Dict: cards
    """
    if os.getenv('TEST'):
        with open(path or '../data/get_cards_test', 'r') as file:
            result = json.load(file)
    else:
        result = MagicTheGatheringAPIClient.get_cards(url=url or 'https://api.magicthegathering.io/v1/cards')
    return result


def __group_by_key(
        data: list,
        key: str,
) -> Dict[str, list]:
    """
    Group elements from a list by

    :param data:
    :param key:
    :return:
    """
    result = defaultdict(list)
    for item in data:
        result[item[key]].append(item)
    return result


def get_cards_with_set(
        url: str = None,
        path: str = None,
):
    data = __get_cards(url=url, path=path)
    data = data.get('cards')
    return __group_by_key(data=data, key='set')


def get_cards_with_set_rarity(
        url: str = None,
        path: str = None,
):
    data = get_cards_with_set(url=url, path=path)

    result = dict()
    for key in data.keys():
        result[key] = __group_by_key(data=data[key], key='rarity')

    return result
