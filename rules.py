import numpy as np

from card import Card, Suit
from card import Rank
from player import Player


class Stich:
    def __init__(self, first_played_card: Card, player: Player):
        self.first_card_played: Card = first_played_card
        self.leading_suit: Suit = first_played_card.suit
        self.played_cards: dict[Card, Player] = {first_played_card: player}

    def add_card(self, card: Card, player: Player):
        self.played_cards[card] = player


class Rules:
    def __init__(self):
        self.deck = self.get_all_cards()
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
        self.rank_order = [
            Rank.ASS,
            Rank.ZEHN,
            Rank.KONIG,
            Rank.NEUN
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
    def get_all_cards():
        return [Card(suit, rank) for suit in Suit for rank in Rank]

    @staticmethod
    def is_trump(card: Card) -> bool:
        return card.rank in [Rank.OBER, Rank.UNTER] or card.suit == Suit.HERZ

    def deal_cards(self) -> list[list[Card]]:
        np.random.shuffle(self.deck)
        return [self.deck[6 * i: 6 * (i + 1)] for i in range(4)]

    def get_trumps_order(self, card: Card):
        return self.trump_order[::-1].index(card)

    def get_card_rank_order(self, rank: Rank):
        return self.rank_order[::-1].index(rank)

    def compare_cards(self, card1: Card, card2: Card, led_suit: Suit):
        trump_card1 = self.is_trump(card1)
        trump_card2 = self.is_trump(card2)
        if card1 == card2:
            raise ValueError("Both cards are equal, which should not happen in a valid game.")
        if trump_card1 and trump_card2:
            # both cards are trump, so the one with the higher order wins
            if self.get_trumps_order(card1) > self.get_trumps_order(card2):
                return card1
            else:
                return card2
        elif trump_card1 and not trump_card2:
            # card1 is trump, card2 is not, so card1 wins
            return card1
        elif not trump_card1 and trump_card2:
            # card2 is trump, card1 is not, so card2 wins
            return card2
        else:
            # both cards are not trump, so leading suit decides
            if card1.suit == led_suit and card2.suit == led_suit:
                # both cards are of the leading suit, so the one with the higher rank wins
                if self.get_card_rank_order(card1.rank) > self.get_card_rank_order(card2.rank):
                    return card1
                else:
                    return card2
            if card1.suit == led_suit and card2.suit != led_suit:
                # card1 is of the leading suit, so it wins
                return card1
            elif card1.suit != led_suit and card2.suit == led_suit:
                # card2 is of the leading suit, so it wins
                return card2
            else:
                # both cards are not of the leading suit, so the first card wins
                return card1

    def determine_winner_on_stich(self, stich: Stich) -> (Player, Card):
        led_suit: Suit = stich.leading_suit
        winning_card: Card = stich.first_card_played

        # compare all played cards
        for challenging_card in stich.played_cards.keys():
            if challenging_card != winning_card:
                winning_card = self.compare_cards(winning_card, challenging_card, led_suit)
        return stich.played_cards[winning_card], winning_card

    def valid_moves(self, hand: list[Card], led_card: Card):
        if not led_card:
            # first card played, so all cards are valid
            return hand
        else:
            if self.is_trump(led_card):
                # trumpf angespielt
                # led card is a trump, so trumps must be played if available
                trumps_on_hand = [card for card in hand if self.is_trump(card)]
                if trumps_on_hand:
                    return trumps_on_hand
                else:
                    return hand
            else:
                # farbe angespielt
                # led card is not a trump, so a card of the leading suit must be played if available
                leading_suits_cards = [card for card in hand if card.suit == led_card.suit]
                if leading_suits_cards:
                    return leading_suits_cards
                else:
                    return hand

    def get_points(self, card: Card):
        return self.points_per_card[card.rank]
