import copy
import random
from enum import Enum


# enum for the suits
class Suit(Enum):
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4

    def __str__(self):
        return self.name


# enum for the faces
# TODO: Figure out how to change values of J, Q and K to 10 when scoring
class Face(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

    def __str__(self):
        return self.name


# object for each card that contains a face and suit
class Card:
    def __init__(self, name: Face, suit: Suit):
        self.name = name
        self.suit = suit

    def get_name(self):
        return self.name

    def get_suit(self):
        return self.suit

    def __str__(self):
        return str(self.name) + " OF " + str(self.suit)


class Deck:
    # deck is hardcoded to be a normal deck of 52 cards
    def __init__(self):
        self.d = []
        x = 1
        while x <= 13:
            self.d.append(Card(Face(x), Suit.CLUBS))
            self.d.append(Card(Face(x), Suit.DIAMONDS))
            self.d.append(Card(Face(x), Suit.HEARTS))
            self.d.append(Card(Face(x), Suit.SPADES))
            x += 1


test = Deck()
print(str(random.choice(test.d)))
"""
class Hand:
    def __init__(self, size: int, hand_cards: Card):
        self.size = size
        self.hand_cards = hand_cards[size]

    def __str__(self):
        hand_string = ""
        for card in self.hand_cards:
            hand_string = hand_string + str(card)


"""
