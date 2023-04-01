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



def check_points(my_hands,sets):
    ranks_dict = {'K': 13, 'Q': 12, 'J': 11, '10': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'A': 1}
    sublists = sets 
    big_list = [item for sublist in sublists for item in sublist]
    points = 0
    for card in my_hands:
        if card not in big_list:
            rank = card[:-3].strip() # get the rank of the card (e.g., 'K' from 'K Bích')
            points += ranks_dict.get(rank, 0) # add the corresponding point value to the total points
    return points

def has_set(my_hands):
    ranks_dict = {'K': 13, 'Q': 12, 'J': 11, '10': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'A': 1}
    # Break sublist to the main list

    sets = []
    
    for i in range(len(my_hands)):
        for j in range(i+1, len(my_hands)):
            for k in range(j+1, len(my_hands)):
                # if cards have equal points
                if my_hands[i][0] == my_hands[j][0] == my_hands[k][0]:
                    sets.append([my_hands[i], my_hands[j], my_hands[k]])
                # Check if other cards not in triple sets already then create new sets
                sublists = sets 
                big_list = [item for sublist in sublists for item in sublist]
                if my_hands[i] not in big_list and my_hands[j] not in big_list and my_hands[k] not in big_list:
                    point_i = ranks_dict.get(my_hands[i][0], 0)
                    point_j = ranks_dict.get(my_hands[j][0], 0)
                    point_k = ranks_dict.get(my_hands[k][0], 0)
                    # i j k
                    # j i k
                    # i k j
                    # j k i
                    # k j i
                    # k i j
                    if (point_i == (point_j - 1) and point_j == (point_k - 1) and point_k == (point_i + 2)) and my_hands[i][2:] == my_hands[j][2:] == my_hands[k][2:] or \
                        (point_j == (point_i - 1) and point_i == (point_k - 1) and point_k == (point_j + 2)) and my_hands[i][2:] == my_hands[j][2:] == my_hands[k][2:] or \
                        (point_i == (point_k - 1) and point_k == (point_j - 1) and point_j == (point_i + 2)) and my_hands[i][2:] == my_hands[j][2:] == my_hands[k][2:] or \
                        (point_j == (point_k - 1) and point_k == (point_i - 1) and point_i == (point_j + 2)) and my_hands[i][2:] == my_hands[j][2:] == my_hands[k][2:] or \
                        (point_k == (point_j - 1) and point_j == (point_i - 1) and point_i == (point_k + 2)) and my_hands[i][2:] == my_hands[j][2:] == my_hands[k][2:] or \
                        (point_k == (point_i - 1) and point_i == (point_j - 1) and point_j == (point_k + 2)) and my_hands[i][2:] == my_hands[j][2:] == my_hands[k][2:]:
                        sets.append([my_hands[i], my_hands[j], my_hands[k]])
                for l in range(k+1, len(my_hands)):
                    if my_hands[i][0] == my_hands[j][0] == my_hands[k][0] == my_hands[l][0]:
                        sets.append([my_hands[i], my_hands[j], my_hands[k], my_hands[l]])
                    
    return sets if sets else []

def has_potential_set(my_hands, sets):
    ranks_dict = {'K': 13, 'Q': 12, 'J': 11, '10': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'A': 1}
    # Break sublist to the main list
    sublists = sets 
    big_list = [item for sublist in sublists for item in sublist]
    pot_sets = []
    for i in range(len(my_hands)):
        if my_hands[i] not in big_list:
            for j in range(i + 1, len(my_hands)):
                if my_hands[j] not in big_list and my_hands[i][0] == my_hands[j][0]:
                    pot_sets.append([my_hands[i], my_hands[j]])

                point_i = ranks_dict.get(my_hands[i][0], 0)
                point_j = ranks_dict.get(my_hands[j][0], 0)
                if my_hands[j] not in big_list and my_hands[j] not in pot_sets and my_hands[i] not in pot_sets and \
                        (point_i == (point_j + 1) and my_hands[i][2:] == my_hands[j][2:]) or \
                    my_hands[j] not in big_list and my_hands[j] not in pot_sets and my_hands[i] not in pot_sets and \
                        (point_j == (point_i + 1) and my_hands[i][2:] == my_hands[j][2:]):
                    pot_sets.append([my_hands[i], my_hands[j]])
        else:
            continue
    return pot_sets if pot_sets else []


def draw_card(deck, recieved_card, potential_set):
    ranks_dict = {'K': 13, 'Q': 12, 'J': 11, '10': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'A': 1}
    if recieved_card not in potential_set:
        if ranks_dict.get(recieved_card, 0) > 8:
            drawed_card = deck.pop()
        else:
            drawed_card = recieved_card
    else:
        drawed_card = recieved_card
    return drawed_card

# Turn
def turn_draw(my_hands, drawed_card):
    my_hands.append(drawed_card)
    return my_hands

def turn_play(my_hands, sets, potential_sets):
    cards_in_sets = []
    for s in sets + potential_sets:
        cards_in_sets += s
    merged_sets = list(set([card for s in sets+potential_sets for card in s]))
    cards_to_keep = list(set(my_hands) - set(merged_sets))
    if not cards_to_keep:
        return None
    cards_points = {card: check_points([card],sets) for card in cards_to_keep}
    card_to_drop = max(cards_points, key=cards_points.get)
    my_hands.remove(card_to_drop)
    return card_to_drop, my_hands





def main():
    # Dealing turn
    print("")
    deck = generate_deck()
    my_hands = deal_cards(deck, 1)[0] # deal 9 cards to the AI player
    sets = has_set(my_hands)
    points = check_points(my_hands, sets)
    potential_set = has_potential_set(my_hands, sets)
    print(f"Your hand: {my_hands}")
    print(f"Points: {points}")
    print("Sets:", sets)
    print("Potential sets:", potential_set)
    print("")
    print("---------------------------------------------------------------------------------------------")

    # Turn 1
    print("")
    print("___Turn 1___")
    print("")
    #
    recieved_card = deck.pop()
    drawed_card = draw_card(deck,recieved_card,potential_set)
    print("Recieved card:", recieved_card)
    print("Drawed card:", drawed_card)
    #
    my_hands = turn_draw(my_hands, drawed_card)
    print(f"Your hand: {my_hands}")
    #
    sets = has_set(my_hands)
    print("Sets:", sets)
    #
    potential_set = has_potential_set(my_hands, sets)
    print("Potential sets:", potential_set)
    #
    points = check_points(my_hands, sets)
    print(f"Points: {points}")
    #
    card_to_drop, my_hands = turn_play(my_hands, sets, potential_set)
    print("Card to drop:", card_to_drop)
    print("Your hands after played: ", my_hands)

    points = check_points(my_hands, sets)
    print(f"Points: {points}")
    print("---------------------------------------------------------------------------------------------")

    # Turn 2
    print("")
    print("___Turn 2___")
    print("")
    #
    recieved_card = deck.pop()
    drawed_card = draw_card(deck,recieved_card,potential_set)
    print("Recieved card:", recieved_card)
    print("Drawed card:", drawed_card)
    #
    my_hands = turn_draw(my_hands, drawed_card)
    print(f"Your hand: {my_hands}")
    #
    sets = has_set(my_hands)
    print("Sets:", sets)
    #
    potential_set = has_potential_set(my_hands, sets)
    print("Potential sets:", potential_set)
    #
    points = check_points(my_hands, sets)
    print(f"Points: {points}")
    #
    card_to_drop, my_hands = turn_play(my_hands, sets, potential_set)
    print("Card to drop:", card_to_drop)
    print("Your hands after played: ", my_hands)
    points = check_points(my_hands, sets)
    print(f"Points: {points}")
    print("---------------------------------------------------------------------------------------------")

    # Turn 3
    print("")
    print("___Turn 3___")
    print("")
    #
    recieved_card = deck.pop()
    drawed_card = draw_card(deck,recieved_card,potential_set)
    print("Recieved card:", recieved_card)
    print("Drawed card:", drawed_card)
    #
    my_hands = turn_draw(my_hands, drawed_card)
    print(f"Your hand: {my_hands}")
    #
    sets = has_set(my_hands)
    print("Sets:", sets)
    #
    potential_set = has_potential_set(my_hands, sets)
    print("Potential sets:", potential_set)
    #
    points = check_points(my_hands, sets)
    print(f"Points: {points}")
    #
    card_to_drop, my_hands = turn_play(my_hands, sets, potential_set)
    print("Card to drop:", card_to_drop)
    print("Your hands after played: ", my_hands)
    points = check_points(my_hands, sets)
    print(f"Points: {points}")
    print("---------------------------------------------------------------------------------------------")

    # Turn 4
    print("")
    print("___Turn 4___")
    print("")
    #
    recieved_card = deck.pop()
    drawed_card = draw_card(deck,recieved_card,potential_set)
    print("Recieved card:", recieved_card)
    print("Drawed card:", drawed_card)
    #
    my_hands = turn_draw(my_hands, drawed_card)
    print(f"Your hand: {my_hands}")
    #
    sets = has_set(my_hands)
    print("Sets:", sets)
    #
    potential_set = has_potential_set(my_hands, sets)
    print("Potential sets:", potential_set)
    #
    points = check_points(my_hands, sets)
    print(f"Points: {points}")
    #
    card_to_drop, my_hands = turn_play(my_hands, sets, potential_set)
    print("Card to drop:", card_to_drop)
    print("Your hands after played: ", my_hands)
    points = check_points(my_hands, sets)
    print(f"Points: {points}")
    print("---------------------------------------------------------------------------------------------")





main()
