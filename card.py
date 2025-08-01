from enum import IntEnum


class Rank(IntEnum):
    OBER = 0
    UNTER = 1
    ASS = 2
    KONIG = 3
    ZEHN = 4
    NEUN = 5


class Suit(IntEnum):
    EICHEL = 0
    BLATT = 1
    HERZ = 2
    SCHELLE = 3


class Card:
    def __init__(self, suit: Suit, rank: Rank):
        self.suit: Suit = suit  # e.g. "Eichel"
        self.rank: Rank = rank  # e.g. "Ass"

    def __repr__(self):
        return f"{self.suit.name} {self.rank.name}"