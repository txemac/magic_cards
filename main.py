import argparse

from src import cards


def run(by_set=False, by_rarity=False):
    result = None
    if by_set is True:
        result = cards.get_cards_with_set()

    elif by_rarity is True:
        result = cards.get_cards_with_set_rarity()

    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Magic the Gathering API client.")
    parser.add_argument('--by_set', action='store_true', required=False)
    parser.add_argument('--by_rarity', action='store_true', required=False)

    args = parser.parse_args()
    run(**vars(args))
