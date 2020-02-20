from src import cards

if __name__ == '__main__':
    print('\n************ Magic: The Gathering API client. ***************\n')
    print(' [a] get cards grouped by set.')
    print(' [b] get cards grouped by set and rarity.')
    print(' [c] get cards filter by rarity KTK and with colours Blue and Red.')
    keypressed = input(' Select option: ')

    result = None
    if keypressed in ['a', 'A']:
        print(' Option: a')
        result = cards.get_cards_with_set()
        print(f' Groups:')
        for item in result:
            print(f'  - {item}: {len(result[item])} item/s.')

    elif keypressed in ['b', 'B']:
        print(' Option: b')
        result = cards.get_cards_with_set_rarity()
        print(f' Groups:')
        for item in result:
            print(f'  - {item}:')
            for subitem in result[item]:
                print(f'     - {subitem}: {len(result[item])} item/s.')

    elif keypressed in ['c', 'C']:
        print(' Option: c')
        result = cards.get_cards_ktk_with_colors()
        print(f' {len(result)} item/s.')

    if input(' Press \'m\' for read the total result: ') == 'm':
        print(result)
