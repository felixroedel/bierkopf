from unittest import TestCase

from game_logic.card import Card
from game_logic.card import Suit, Rank
from game_logic.player import Player

from game_logic.rules import Rules, Stich


class CardTestCase(TestCase):
    def test_card_creation(self):
        card = Card(Suit.HERZ, Rank.NEUN)
        self.assertEqual(card.suit, "Herz")
        self.assertEqual(card.rank, "9")

    def test_card_str(self):
        card = Card(Suit.EICHEL, Rank.ASS)
        self.assertEqual(card.__repr__(), "Eichel Ass")

    # todo: make a card available only once
    def test_card_equality(self):
        card1 = Card(Suit.BLATT, Rank.KONIG)
        card2 = Card(Suit.BLATT, Rank.KONIG)
        self.assertEqual(card1, card2)


class RulesTestCase(TestCase):
    def setUp(self):
        self.rules = Rules()

    def test_is_trump(self):
        self.assertTrue(self.rules.is_trump(Card(Suit.HERZ, Rank.ASS)))
        self.assertTrue(self.rules.is_trump(Card(Suit.EICHEL, Rank.OBER)))
        self.assertFalse(self.rules.is_trump(Card(Suit.EICHEL, Rank.ASS)))

    def test_deal_cards(self):
        hands = self.rules.deal_cards()
        self.assertEqual(len(hands), 4)
        for hand in hands:
            self.assertEqual(len(hand), 6)
        all_cards = [card for hand in hands for card in hand]
        self.assertEqual(len(set(all_cards)), 24)

    def test_compare_cards_trump(self):
        card1 = Card(Suit.HERZ, Rank.OBER)
        card2 = Card(Suit.HERZ, Rank.UNTER)
        led_suit = Suit.HERZ
        winner = self.rules.compare_cards(card1, card2, led_suit)
        self.assertEqual(winner, card1)

    def test_compare_cards_leading_suit(self):
        card1 = Card(Suit.EICHEL, Rank.ASS)
        card2 = Card(Suit.EICHEL, Rank.KONIG)
        led_suit = Suit.EICHEL
        winner = self.rules.compare_cards(card1, card2, led_suit)
        self.assertEqual(winner, card1)

    def test_get_points(self):
        self.assertEqual(self.rules.get_points(Card(Suit.HERZ, Rank.ASS)), 11)
        self.assertEqual(self.rules.get_points(Card(Suit.HERZ, Rank.OBER)), 3)
        self.assertEqual(self.rules.get_points(Card(Suit.HERZ, Rank.NEUN)), 0)

    def test_valid_moves_trump(self):
        hand = [
            Card(Suit.HERZ, Rank.ASS),
            Card(Suit.EICHEL, Rank.ASS),
            Card(Suit.HERZ, Rank.OBER),
        ]
        led_card = Card(Suit.HERZ, Rank.ZEHN)
        valid = self.rules.get_valid_moves(hand, led_card)
        self.assertIn(Card(Suit.HERZ, Rank.ASS), valid)
        self.assertIn(Card(Suit.HERZ, Rank.OBER), valid)
        self.assertNotIn(Card(Suit.EICHEL, Rank.ASS), valid)

    def test_valid_moves_leading_suit(self):
        hand = [
            Card(Suit.EICHEL, Rank.ASS),
            Card(Suit.BLATT, Rank.ASS),
            Card(Suit.HERZ, Rank.OBER),
            Card(Suit.EICHEL, Rank.ZEHN)
        ]
        led_card = Card(Suit.EICHEL, Rank.KONIG)
        valid = self.rules.get_valid_moves(hand, led_card)
        self.assertIn(Card(Suit.EICHEL, Rank.ASS), valid)
        self.assertIn(Card(Suit.EICHEL, Rank.ZEHN), valid)
        self.assertNotIn(Card(Suit.BLATT, Rank.ASS), valid)
        self.assertNotIn(Card(Suit.HERZ, Rank.OBER), valid)

    def test_determine_winner_on_stich(self):
        player1 = Player("A")
        player2 = Player("B")
        player3 = Player("C")
        player4 = Player("D")
        stich = Stich(Card(Suit.HERZ, Rank.ASS), player1)
        stich.add_card(Card(Suit.HERZ, Rank.KONIG), player2)
        stich.add_card(Card(Suit.BLATT, Rank.ZEHN), player3)
        stich.add_card(Card(Suit.HERZ, Rank.NEUN), player4)
        winner, winning_card, points = self.rules.determine_winner_on_stich(stich)
        self.assertEqual(winner, player1)
        self.assertEqual(winning_card, Card(Suit.HERZ, Rank.ASS))
        self.assertEqual(points, 25)
