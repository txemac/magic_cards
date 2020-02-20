import pytest

from data.api_magic_client import MagicTheGatheringAPIClient
from src import cards


@pytest.mark.skip
def test_get_cards():
    data1 = MagicTheGatheringAPIClient.get_cards(url='https://api.magicthegathering.io/v1/cards')
    data2 = cards.__get_cards(path='../data/get_cards.py')
    assert data1 == data2


def test_group_by_key_set(data_example):
    expected = dict(
        set_a=[dict(set='set_a', rarity='rarity_3'), dict(set='set_a', rarity='rarity_4')],
        set_b=[dict(set='set_b', rarity='rarity_4'), dict(set='set_b', rarity='rarity_5')],
    )
    assert cards.__group_by_key(data=data_example, key='set') == expected
