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

def discard_cards(hand):
    set_types = {'three-of-a-kind': 3, 'four-of-a-kind': 4}
    for set_type, set_size in set_types.items():
        for i in range(len(hand)-set_size+1):
            set_cards = hand[i:i+set_size]
            ranks = [card[:-3].strip() for card in set_cards]
            if len(set(ranks)) == 1:
                # discard all cards that are not part of the set
                for card in set_cards:
                    hand.remove(card)

def check_points(hand):
    ranks_dict = {'K': 13, 'Q': 12, 'J': 11, '10': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'A': 1}
    points = 0
    for card in hand:
        rank = card[:-3].strip() # get the rank of the card (e.g., 'K' from 'K Bích')
        points += ranks_dict.get(rank, 0) # add the corresponding point value to the total points
    return points

def ai_player():
    deck = generate_deck()
    my_hand = deal_cards(deck, 1)[0] # deal 9 cards to the AI player
    discard_cards(my_hand) # discard any cards that are not part of a valid set
    points = check_points(my_hand)
    print(f"AI player's hand: {my_hand}")
    print(f"AI player's points: {points}")

if __name__ == '__main__':
    ai_player()
