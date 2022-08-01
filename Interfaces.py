from os import system, name


def clear():
    """Clears the the prompt.
    """
    system('cls' if name == 'nt' else 'clear')


def menu():
    """The UNO game menu and its options.
    Returns the exit value(101) or the int of the number of players(plus the user).
    """
    def title():
        clear()
        print('¨' * 64)
        print(f'{"UNO":^64}')
        print('_' * 64 + '\n')

    while True:
        title()
        while True:
            choice = input('1 - Play\n2 - Tutorial\n3 - Exit\nYour choice: ')
            if not choice.isnumeric() or int(choice) > 3 or int(choice) < 1:
                print('\nPlease, enter a valid option')
                continue
            break
        if int(choice) == 1:
            title()
            while True:
                playernum = input('How many players do you wish to play against? (min:1/max:3) ')
                if not playernum.isnumeric() or int(playernum) > 3 or int(playernum) < 1:
                    print('\nPlease, enter a valid number')
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
    """Shows the Game interface.

    Args:
        qnt_of_players (int): the number of players in the game (min:2, max:4). 
        hand (list of Card()): the list of cards the player has in hand.
        last_played (Card()): the last played card.
        turn (int): the turn (min:1, max:qnt_of_players).
        qnt_of_cards (dict): dictionary containing each player's card quantity.
    """
    clear()
    if qnt_of_players == 2:
        if turn == 1:
            arrow = "v"
        elif turn == 2:
            arrow = "^"
        print(f'{qnt_of_cards["Player 2"]:^64}\n\n{arrow:^64}\n')
    elif qnt_of_players == 3:        
        if turn == 1:
            arrow = 'v'
        elif turn == 2:
            arrow = '<'
        elif turn == 3:
            arrow = '>'
        print(f'\n\n{qnt_of_cards["Player 2"]:<2}{arrow:^60}{qnt_of_cards["Player 3"]:>2}\n')
    elif qnt_of_players == 4:
        if turn == 1:
            arrow = "v"
        elif turn == 2:
            arrow = "<"
        elif turn == 3:
            arrow = "^"
        elif turn == 4:
            arrow = ">"
        print(f'{qnt_of_cards["Player 3"]:^64}\n\n')
        print(f'{qnt_of_cards["Player 2"]:<2}{arrow:^60}{qnt_of_cards["Player 4"]:>2}\n')
    print(f'{"_________":^64}\n{"|       |":^64}\n{f"|{last_played.effect():^7}|":^64}'
          f'\n{f"|{last_played.get_color():^7}|":^64}\n{"|       |":^64}\n{"¨¨¨¨¨¨¨¨¨":^64}\n\n')
    if turn == 1:
        for position in range(0, len(hand), 6):
            if len(hand) - position >= 6:
                qnt = 6
            else:
                qnt = len(hand) - position
            print('_________  ' * qnt)
            for number in range(position, position + qnt):
                print(f'|{number + 1:<7}|', end='  ')
            print()
            for card in range(position, position + qnt):
                print(f'|{hand[card].effect():^7}|', end='  ')
            print()
            for card in range(position, position + qnt):
                print(f'|{hand[card].get_color():^7}|', end='  ')
            print('\n' + '|       |  ' * qnt + '\n' + '¨¨¨¨¨¨¨¨¨  ' * qnt)
    else:
        print(f'{qnt_of_cards["Player 1"]:^64}')