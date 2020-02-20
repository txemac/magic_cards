import os

import pytest

os.environ['TEST'] = '1'


@pytest.fixture
def data_example():
    return [
        dict(set='set_a', rarity='rarity_3'),
        dict(set='set_a', rarity='rarity_4'),
        dict(set='set_b', rarity='rarity_4'),
        dict(set='set_b', rarity='rarity_5'),
    ]
