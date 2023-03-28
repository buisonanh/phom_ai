import random
import numpy as np

class RLPlayer:
    def __init__(self, num_actions, alpha=0.1, gamma=1.0, epsilon=0.1):
        self.Q = np.zeros((num_actions, num_actions))
        self.alpha = alpha # learning rate
        self.gamma = gamma # discount factor
        self.epsilon = epsilon # exploration rate
    
    def get_action(self, state):
        # epsilon-greedy policy
        if np.random.uniform(0, 1) < self.epsilon:
            return np.random.randint(len(state))
        else:
            values = self.Q[state, :]
            return np.random.choice(np.flatnonzero(values == values.max()))
    
    def update(self, state, action, reward, next_state):
        # Q-learning update rule
        self.Q[state, action] += self.alpha * (reward + self.gamma * np.max(self.Q[next_state, :]) - self.Q[state, action])

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

def ai_player(num_episodes=1000):
    # initialize RL player
    num_actions = 9
    rl_player = RLPlayer(num_actions)
    
    for episode in range(num_episodes):
        # generate a new deck and deal cards to the AI player
        deck = generate_deck()
        my_hand = deal_cards(deck, 1)[0]
        
        # discard any cards that are not part of a valid set
        discard_cards(my_hand)
        
        # initialize state and points
        state = len(my_hand)
        points = check_points(my_hand)
        
        while True:
            # AI player selects an action
            action = rl_player.get_action(state)
            
                        # execute action
            cards_to_discard = my_hand[:action]
            for card in cards_to_discard:
                my_hand.remove(card)
            new_cards = deck[:action]
            for card in new_cards:
                my_hand.append(card)
            deck = deck[action:] + cards_to_discard
            
            # discard any cards that are not part of a valid set
            discard_cards(my_hand)
            
            # calculate reward and next state
            new_points = check_points(my_hand)
            reward = new_points - points
            points = new_points
            next_state = len(my_hand)
            
            # update Q-value
            rl_player.update(state, action, reward, next_state)
            
            # check if game is over
            if len(deck) == 0:
                break
            
            # update state
            state = next_state
        
    return rl_player

