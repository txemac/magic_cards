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


def test_group_by_key_rarity(data_example):
    expected = dict(
        rarity_3=[dict(set='set_a', rarity='rarity_3')],
        rarity_4=[dict(set='set_a', rarity='rarity_4'), dict(set='set_b', rarity='rarity_4')],
        rarity_5=[dict(set='set_b', rarity='rarity_5')],
    )
    assert cards.__group_by_key(data=data_example, key='rarity') == expected


def test_get_cards_with_set():
    result = cards.get_cards_with_set(path='../data/get_cards_test.py')
    assert len(result) == 2
    assert list(result.keys()) == ['10E', 'KTK']
    assert isinstance(result['10E'], list)
    assert isinstance(result['KTK'], list)
    assert result['10E'][0]['name'] == 'Abundance'
    assert result['10E'][1]['name'] == 'Academy Researchers'
    assert result['KTK'][0]['name'] == 'Avalanche Tusker'
    assert result['KTK'][1]['name'] == 'Bear\'s Companion'


def test_get_cards_with_set_rarity():
    result = cards.get_cards_with_set_rarity(path='../data/get_cards_test.py')
    assert len(result) == 2
    assert list(result.keys()) == ['10E', 'KTK']
    assert isinstance(result['10E'], dict)
    assert isinstance(result['KTK'], dict)
    assert list(result['10E'].keys()) == ['Rare', 'Uncommon']
    assert list(result['KTK'].keys()) == ['Rare', 'Uncommon']
    assert result['10E']['Rare'][0]['name'] == 'Abundance'
    assert result['10E']['Uncommon'][0]['name'] == 'Academy Researchers'
    assert result['KTK']['Rare'][0]['name'] == 'Avalanche Tusker'
    assert result['KTK']['Uncommon'][0]['name'] == 'Bear\'s Companion'
