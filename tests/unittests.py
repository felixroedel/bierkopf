from unittest import TestCase

from card import Card
from card import Suit, Rank

from rules import Rules


class CardTestCase(TestCase):
    def test_card_creation(self):
        card = Card(Suit.HERZ, Rank.NEUN)
        self.assertEqual(card.suit, "Herz")
        self.assertEqual(card.rank, "9")

    def test_card_str(self):
        card = Card(Suit.EICHEL, Rank.ASS)
        self.assertEqual(card.__repr__(), "Eichel Ass")

    # todo: make a card available only once
    # def test_card_equality(self):
    #     card1 = Card(Suit.BLATT, Rank.KONIG)
    #     card2 = Card(Suit.BLATT, Rank.KONIG)
    #     self.assertEqual(card1, card2)


class RulesTestCase(TestCase):
    pass
