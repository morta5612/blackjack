import copy
from enum import Enum


class Suit(Enum):
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4

    def __str__(self):
        return self.name


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
    JACK = 10
    QUEEN = 10
    KING = 10

    def __str__(self):
        return self.name


class Card:
    def __init__(self, name: Face, suit: Suit):
        self.name = name
        self.suit = suit

    def get_name(self):
        return self.name

    def get_suit(self):
        return self.suit

    def __getitem__(self, item):
        c = copy.copy(self)
        c.name = self.get_name()[item]
        c.suit = self.get_suit()[item]
        return c

    def __str__(self):
        return str(self.name) + " OF " + str(self.suit)


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
