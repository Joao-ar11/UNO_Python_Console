from os import system, name


def clear():
    system('cls' if name == 'nt' else 'clear')


def menu():
    def title():
        clear()
        print('¨' * 61)
        print(f'{"UNO":^61}')
        print('_' * 61 + '\n')

    while True:
        title()
        while True:
            choice = input('1 - Play\n2 - Tutorial\n3 - Exit\nYour choice: ')
            if not choice.isnumeric() or int(choice) > 3 or int(choice) < 1:
                print('Please, enter a valid option')
                continue
            break
        if int(choice) == 1:
            title()
            while True:
                playernum = input('How many players do you wish to play against? (min:1/max:3) ')
                if not playernum.isnumeric() or int(playernum) > 3 or int(playernum) < 1:
                    print('Please, enter a valid number')
                    continue
                break
            return int(playernum) + 1
        elif int(choice) == 2:
            title()
            print("The rules are the same as the normal UNO game, but you don't\n"
                    "need to shout UNO if you have only one card. To play one of\n"
                    "you card you only need to type the number o the top left of it\n"
                    "and then press enter to play it.")
            print("Special commands:\n  101 - Exit\n  99 - Pick a card from the deck\n")
            input('Press Enter to cotinue')
        elif int(choice) == 3:
            return 101


def interface(qnt_of_players, hand, last_played, turn, qnt_of_cards):
    if qnt_of_players == 2:
        if turn == 1:
            arrow = "v"
        elif turn == 2:
            arrow = "^"
        print(f'{qnt_of_cards["Player 2"]:^61}\n\n{arrow:^61}\n')
    elif qnt_of_players == 3:        
        if turn == 1:
            arrow = 'v'
        elif turn == 2:
            arrow = '<'
        elif turn == 3:
            arrow = '>'
        print(f'\n\n{qnt_of_cards["Player 2"]:<2}{arrow:^57}{qnt_of_cards["Player 3"]:>2}\n')
    elif qnt_of_players == 4:
        if turn == 1:
            arrow = "v"
        elif turn == 2:
            arrow = "<"
        elif turn == 3:
            arrow = "^"
        elif turn == 4:
            arrow = ">"
        print(f'{qnt_of_cards["Player 3"]:^61}\n\n')
        print(f'{qnt_of_cards["Player 2"]:<2}{arrow:^57}{qnt_of_cards["Player 4"]:>2}\n')

interface(4, [1, 2, 3], 4, 4, {'Player 1': 5, 'Player 2': 2, 'Player 3': 3, 'Player 4': 4})