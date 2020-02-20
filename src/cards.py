from collections import defaultdict
from typing import Dict
from typing import List

from data.api_magic_client import MagicTheGatheringAPIClient


def __group_by_key(
        data: List,
        key: str,
) -> Dict[str, List]:
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


def get_cards_with_set() -> Dict[str, List]:
    """
    Get cards grouped by set.

    :return Dict: groups
    """
    data = MagicTheGatheringAPIClient.get_cards()
    return __group_by_key(data=data.get('cards'), key='set')


def get_cards_with_set_rarity() -> Dict[str, Dict[str, List]]:
    """
    Get cards grouped by set and rarity.

    :return Dict: groups
    """
    data = get_cards_with_set()

    result = dict()
    for key in data.keys():
        result[key] = __group_by_key(data=data[key], key='rarity')

    return result


def get_cards_ktk_with_colors() -> List:
    """
    Get cards filters by set TKT and with colors Blue and Red.

    :return Dict: groups
    """
    data = MagicTheGatheringAPIClient.get_cards()

    return [d for d in data.get('cards')
            if d['set'].lower() == 'ktk' and all(x in d['colors'] for x in ['Red', 'Blue'])]
