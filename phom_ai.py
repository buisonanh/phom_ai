


#names = [' Cơ',' Zô',' Bích',' Tép']
#ranks = ['K','Q','J','10','9','8','7','6','5','4','3','2','A']
#Full_Deck = [f"{rank}{name}" for name in names for rank in ranks]

def insert_hand(): 
    my_hand = []
    for i in range(9):
        card = str(input(f"Card {i+1}: "))
        my_hand.append(card)
    return my_hand



def check_points(my_hand):
    ranks_dict = {'K': 13, 'Q': 12, 'J': 11, '10': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'A': 1}
    points = 0
    for card in my_hand:
        rank = card[:-3].strip() # get the rank of the card (e.g., 'K' from 'K Bích')
        points += ranks_dict.get(rank, 0) # add the corresponding point value to the total points
    return points




def main():
    my_hand = insert_hand()
    points = check_points(my_hand)
    print(f"Your hand: {my_hand}")
    print(f"Points: {points}")

main()
