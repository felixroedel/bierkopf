from numpy import random

from card import Card, Suit
from card import Rank


class Rules:
    def __init__(self):
        self.deck = [
            Card(Suit.EICHEL, Rank.OBER),
            Card(Suit.BLATT, Rank.OBER),
            Card(Suit.HERZ, Rank.OBER),
            Card(Suit.SCHELLE, Rank.OBER),
            Card(Suit.EICHEL, Rank.UNTER),
            Card(Suit.BLATT, Rank.UNTER),
            Card(Suit.HERZ, Rank.UNTER),
            Card(Suit.SCHELLE, Rank.UNTER),
            Card(Suit.HERZ, Rank.ASS),
            Card(Suit.HERZ, Rank.ZEHN),
            Card(Suit.HERZ, Rank.KONIG),
            Card(Suit.HERZ, Rank.NEUN),
            Card(Suit.EICHEL, Rank.ASS),
            Card(Suit.EICHEL, Rank.ZEHN),
            Card(Suit.EICHEL, Rank.KONIG),
            Card(Suit.EICHEL, Rank.NEUN),
            Card(Suit.EICHEL, Rank.ZEHN),
            Card(Suit.BLATT, Rank.ASS),
            Card(Suit.BLATT, Rank.ZEHN),
            Card(Suit.BLATT, Rank.KONIG),
            Card(Suit.BLATT, Rank.NEUN),
            Card(Suit.SCHELLE, Rank.ASS),
            Card(Suit.SCHELLE, Rank.ZEHN),
            Card(Suit.SCHELLE, Rank.KONIG),
            Card(Suit.SCHELLE, Rank.NEUN),
        ]
        self.trump_order = [
            Card(Suit.EICHEL, Rank.OBER),
            Card(Suit.BLATT, Rank.OBER),
            Card(Suit.HERZ, Rank.OBER),
            Card(Suit.SCHELLE, Rank.OBER),
            Card(Suit.EICHEL, Rank.UNTER),
            Card(Suit.BLATT, Rank.UNTER),
            Card(Suit.HERZ, Rank.UNTER),
            Card(Suit.SCHELLE, Rank.UNTER),
            Card(Suit.HERZ, Rank.ASS),
            Card(Suit.HERZ, Rank.ZEHN),
            Card(Suit.HERZ, Rank.KONIG),
            Card(Suit.HERZ, Rank.NEUN),
        ]
        self.points_per_card = {
            Rank.OBER: 3,
            Rank.UNTER: 2,
            Rank.ASS: 11,
            Rank.ZEHN: 10,
            Rank.KONIG: 4,
            Rank.NEUN: 0,
        }

    @staticmethod
    def is_trump(card: Card) -> bool:
        return card.rank in [Rank.OBER, Rank.UNTER] or card.suit == Suit.HERZ

    def deal_cards(self) -> list[list[Card]]:
        random.shuffle(self.deck)
        return [self.deck[6 * i: 6 * (i + 1)] for i in range(4)]
