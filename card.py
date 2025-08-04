from enum import StrEnum


class Rank(StrEnum):
    OBER = "Ober"
    UNTER = "Unter"
    ASS = "Ass"
    KONIG = "König"
    ZEHN = "10"
    NEUN = "9"


class Suit(StrEnum):
    EICHEL = "Eichel"
    BLATT = "Blatt"
    HERZ = "Herz"
    SCHELLE = "Schelle"


class Card:
    def __init__(self, suit: Suit, rank: Rank):
        self.suit: Suit = suit  # e.g. "Eichel"
        self.rank: Rank = rank  # e.g. "Ass"

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"{self.suit} {self.rank}"

    def __hash__(self):
        return hash(self.__str__())

    def __eq__(self, other):
        if not isinstance(other, Card):
            raise TypeError(f"Cannot compare card with type {type(other)}")
        return other.suit == self.suit and other.rank == self.rank
