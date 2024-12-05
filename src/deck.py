import random
from src.card import Card

class Deck:
    def __init__(self):
        # Create a deck of 52 cards (standard deck)
        self.cards = []
        self.create_deck()

    def create_deck(self):
        # Create all 52 cards (13 ranks for 4 suits)
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]

    def shuffle_deck(self):
        # Shuffle the deck using random.shuffle
        random.shuffle(self.cards)

    def deal_card(self):
        # Deal a card from the deck and remove it from the deck
        if len(self.cards) > 0:
            return self.cards.pop()  # Return the last card from the shuffled deck
        else:
            return None  # If the deck is empty, return None
