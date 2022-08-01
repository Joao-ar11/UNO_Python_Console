from card import Card
import interfaces
from random import shuffle, randint
from time import sleep


while True:
    hand = dict()
    qnt_cards = dict()
    block = 0
    plus = 0
    way = 1
    choice = interfaces.menu()
    if choice == 101:
        break
    print('Loading...')
    qnt_players = choice
    deck = [Card(number, color) for color in range(1, 5) for number in range(0, 13) for _ in range(0, 2)]
    deck.extend([Card(number) for number in range(13, 15) for _ in range(0, 4)])
    shuffle(deck)
    for player in range(1, qnt_players + 1):
        hand[f'Player {player}'] = list()
        for card in range(0, 7):
            hand[f'Player {player}'].append(deck[0])
            deck.pop(0)
        qnt_cards[f'Player {player}'] = len(hand[f'Player {player}'])
    turn = randint(1, qnt_players)
    last_card = deck[0]
    deck.pop(0)
    while qnt_cards[f'Player {turn}'] != 0:
        if turn == 1:
            confirm = False
            if plus == 0 == block:                
                while True:
                    interfaces.interface(qnt_players, hand['Player 1'], last_card, turn, qnt_cards)
                    try:
                        choice = int(input('\nYour choice: ')) - 1
                    except:
                        input('Please, type a valid number')
                        continue                   
                    if choice == 100:
                        break
                    elif choice == 98:
                        if len(deck) > 0:
                            hand['Player 1'].append(deck[0])
                            qnt_cards['Player 1'] += 1
                            deck.pop(0)
                        else:
                            input('There is no more cards to pick!')
                            confirm = True
                            break
                    elif choice < 0 or choice > len(hand['Player 1']) - 1:
                        input('Choose a valid card')
                        continue
                    elif hand['Player 1'][choice].check(last_card): break
                if choice == 100:
                    break
                elif hand['Player 1'][choice].get_color() == 'Black':
                    while True:
                        try:
                            color = int(input('Choose a color (1 - Red, 2 - Blue, 3 - Yellow, 4 - Green): '))
                        except:
                            input('Please, enter a valid number')
                            continue
                        if color < 1 or color > 4:
                            input('Please, enter a valid number')
                            continue
                        break
                    hand['Player 1'][choice].change_color(color)
                    if hand['Player 1'][choice].effect() == '+4':
                        plus += 4
                if hand['Player 1'][choice].effect() == '+2':
                    plus += 2
                if hand['Player 1'][choice].effect() == 'X':
                    block += 1
                if hand['Player 1'][choice].effect() == '<->':
                    way *= -1
                if not confirm:
                    if last_card.temp():
                        last_card.change_color(0)
                    deck.append(last_card)
                    last_card = hand['Player 1'][choice]
                    hand['Player 1'].pop(choice)
                    qnt_cards['Player 1'] -= 1
            elif plus > 0:
                for card in hand['Player 1']:
                    if card.effect() == '+2' or card.effect() == '+4':
                        confirm = True
                        break
                if confirm:
                    while True:
                        interfaces.interface(qnt_players, hand['Player 1'], last_card, turn, qnt_cards)
                        try:
                            choice = int(input('\nYour choice: ')) - 1
                        except:
                            input('Please, type a valid number')
                            continue                       
                        if choice == 100:
                            break
                        elif choice == 98:
                            input("You can't pick cards now")
                        elif choice < 0 or choice > len(hand['Player 1']) - 1:
                            input('Choose a valid card')
                            continue
                        elif hand['Player 1'][choice].effect() == '+2' or hand['Player 1'][choice].effect() == '+4':
                            break
                    if choice == 100:
                        break
                    elif hand['Player 1'][choice].get_color() == 'Black':
                        while True:
                            try:
                                color = int(input('Choose a color (1 - Red, 2 - Blue, 3 - Yellow, 4 - Green): '))
                            except:
                                input('Please, enter a valid number')
                                continue
                            if color < 1 or color > 4:
                                input('Please, enter a valid number')
                                continue
                            break
                        plus += 4
                    elif hand['Player 1'][choice] == '+2':
                        plus += 2
                    if last_card.temp():
                        last_card.change_color(0)
                    deck.append(last_card)
                    last_card = hand['Player 1'][choice]
                    hand['Player 1'].pop(choice)
                    qnt_cards['Player 1'] -= 1
                else:
                    hand['Player 1'].extend(deck[:plus])
                    qnt_cards['Player 1'] += plus
                    for _ in range(0, plus):
                        deck.pop(0)
                    plus = 0
            elif block > 0:
                block = 0
        
        turn += way
        if turn > qnt_players:
            turn = 1
        elif turn == 0:
            turn = qnt_players
            
                
                
print('_' * 64 + '\n')