from typing import Dict

import requests


class MagicTheGatheringAPIClient:

    @staticmethod
    def get_cards(
            url: str = None,
    ) -> Dict:
        """
        Get all cards from Magic The Gathering API.

        :param str url: URL
        :return Dict: cards
        """
        response = requests.get(url=url or 'https://api.magicthegathering.io/v1/cards')
        return response.json()
