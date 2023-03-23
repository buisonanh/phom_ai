import random

def generate_deck():
    names = [' Cơ',' Zô',' Bích',' Tép']
    ranks = ['K','Q','J','10','9','8','7','6','5','4','3','2','A']
    deck = [f"{rank}{name}" for name in names for rank in ranks]
    random.shuffle(deck) # shuffle the deck
    return deck

def deal_cards(deck, num_players):
    player_hands = [[] for i in range(num_players)]
    for i in range(9):
        for j in range(num_players):
            player_hands[j].append(deck.pop())
    return player_hands



def check_points(my_hands):
    ranks_dict = {'K': 13, 'Q': 12, 'J': 11, '10': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'A': 1}
    points = 0
    for card in my_hands:
        rank = card[:-3].strip() # get the rank of the card (e.g., 'K' from 'K Bích')
        points += ranks_dict.get(rank, 0) # add the corresponding point value to the total points
    return points

def has_set(my_hands):
    sets = []
    for i in range(len(my_hands)):
        for j in range(i+1, len(my_hands)):
            for k in range(j+1, len(my_hands)):
                if my_hands[i][0] == my_hands[j][0] == my_hands[k][0]:
                    sets.append([my_hands[i], my_hands[j], my_hands[k]])
    return sets if sets else "None"

def has_pottential_set(my_hands,set):
    sets = []
    for i in range(len(my_hands)):
        for j in range(i+1, len(my_hands)):
                if my_hands[i][0] == my_hands[j][0] and my_hands[i][0] not in set and my_hands[j][0] not in set:
                    sets.append([my_hands[i], my_hands[j]])
    return sets if sets else "None"

def draw_card(deck):
    drawed_card = deck.pop()
    return drawed_card

def turn1_draw(my_hands, drawed_card):
    my_hands.append(drawed_card)
    return my_hands

def turn1_play():
    pass


def main():
    # Dealing turn
    deck = generate_deck()
    my_hands = deal_cards(deck, 1)[0] # deal 9 cards to the AI player
    points = check_points(my_hands)
    sets = has_set(my_hands)
    pottential_set = has_pottential_set(my_hands, sets)
    print(f"Your hand: {my_hands}")
    print(f"Points: {points}")
    print("Sets:", sets)
    print("Pottential sets:", pottential_set)
    print("")

    # Turn 1
    drawed_card = draw_card(deck)
    my_hands = turn1_draw(my_hands, drawed_card)
    sets = has_set(my_hands)
    pottential_set = has_pottential_set(my_hands, sets)
    print("Drawed card:", drawed_card)
    print(f"Your hand: {my_hands}")
    print("Set:", sets)
    print("Pottential sets:", pottential_set)

    card_to_drop = turn1_play(my_hands, sets, pottential_set)
    print("Card to drop:", card_to_drop)


main()
