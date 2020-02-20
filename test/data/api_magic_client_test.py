import pytest

from data.api_magic_client import MagicTheGatheringAPIClient


@pytest.mark.skip
def test_get_cards_url_vs():
    data = MagicTheGatheringAPIClient.get_cards()
    assert len(data.get('cards')) == 100
