
from card import Card

import random

class Deck:
    cards = []
    suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    # Constructor that creates a deck of 52 cards
    def __init__(self):
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(Card(suit, rank))
    
    # Shuffle the deck
    def shuffle(self):
        random.shuffle(self.cards)
    
    # Deal a card from the deck
    def deal(self):
        return self.cards.pop()

