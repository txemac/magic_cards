import pytest


@pytest.fixture
def data_example():
    return [
        dict(set='set_a', rarity='rarity_3'),
        dict(set='set_a', rarity='rarity_4'),
        dict(set='set_b', rarity='rarity_4'),
        dict(set='set_b', rarity='rarity_5'),
    ]


@pytest.fixture
def mock_data(mocker):
    mocked_data = mocker.patch('data.api_magic_client.MagicTheGatheringAPIClient.get_cards')
    mocked_data.return_value = {
        "cards": [
            {
                "name": "Abundance",
                "colors": [
                    "Green"
                ],
                "rarity": "Rare",
                "set": "10E",
                "id": "1669af17-d287-5094-b005-4b143441442f"
            },
            {
                "name": "Academy Researchers",
                "colors": [
                    "Blue"
                ],
                "rarity": "Uncommon",
                "set": "10E",
                "id": "047d5499-a21c-5f5c-9679-1599fcaf9815"
            },
            {
                "name": "Avalanche Tusker",
                "colors": [
                    "Green",
                    "Blue"
                ],
                "rarity": "Rare",
                "set": "KTK",
                "id": "1ac999e7-e607-59e7-8665-3cc1b85ed7c4"
            },
            {
                "name": "Bear's Companion",
                "colors": [
                    "Green",
                    "Red",
                    "Blue"
                ],
                "rarity": "Uncommon",
                "set": "KTK",
                "id": "bdba9c03-6ae8-559e-826d-b6eeee934791"
            }
        ]
    }
