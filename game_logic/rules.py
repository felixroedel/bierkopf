import logging
from enum import IntEnum

import numpy as np

from game_logic.card import Card, Suit
from game_logic.card import Rank
from game_logic.player import Player
from game_logic.stich import Stich


class Multiplier(IntEnum):
    # multiplier given by players
    SPRITZ = 2
    RE = 3
    CONTRA = 4

    # multiplier given by game result
    SCHNEIDER = 2
    SCHWARZ = 3


class Rules:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    trump_order = [
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
    rank_order = [
        Rank.ASS,
        Rank.ZEHN,
        Rank.KONIG,
        Rank.NEUN
    ]
    points_per_card = {
        Rank.OBER: 3,
        Rank.UNTER: 2,
        Rank.ASS: 11,
        Rank.ZEHN: 10,
        Rank.KONIG: 4,
        Rank.NEUN: 0,
    }
    points_per_won_round = {

    }

    @staticmethod
    def get_all_cards():
        return [Card(suit, rank) for suit in Suit for rank in Rank]

    @staticmethod
    def is_trump(card: Card) -> bool:
        return card.rank in [Rank.OBER, Rank.UNTER] or card.suit == Suit.HERZ

    @staticmethod
    def deal_cards() -> list[list[Card]]:
        deck = Rules.get_all_cards()
        np.random.shuffle(deck)
        return [deck[6 * i: 6 * (i + 1)] for i in range(4)]

    @staticmethod
    def get_trumps_order(card: Card):
        return Rules.trump_order[::-1].index(card)

    @staticmethod
    def get_card_rank_order(rank: Rank):
        return Rules.rank_order[::-1].index(rank)

    @staticmethod
    def compare_cards(card1: Card, card2: Card, led_suit: Suit):
        trump_card1 = Rules.is_trump(card1)
        trump_card2 = Rules.is_trump(card2)
        if card1 == card2:
            raise ValueError("Both cards are equal, which should not happen in a valid game.")
        if trump_card1 and trump_card2:
            # both cards are trump, so the one with the higher order wins
            if Rules.get_trumps_order(card1) > Rules.get_trumps_order(card2):
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
                if Rules.get_card_rank_order(card1.rank) > Rules.get_card_rank_order(card2.rank):
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

    @staticmethod
    def determine_winner_on_stich(stich: Stich) -> (Player, Card, int):
        led_suit: Suit = stich.leading_suit
        winning_card: Card = stich.first_card_played
        points: int = 0
        for challenging_card in stich.played_cards.keys():
            points += Rules.get_points(challenging_card)
            if challenging_card != winning_card:
                winning_card = Rules.compare_cards(winning_card, challenging_card, led_suit)
        return stich.played_cards[winning_card], winning_card, points

    @staticmethod
    def get_valid_moves(hand: list[Card], led_card: Card):
        if not led_card:
            # first card played, so all cards are valid
            valid_moves = hand
        else:
            if Rules.is_trump(led_card):
                # trumpf angespielt
                # led card is a trump, so trumps must be played if available
                trumps_on_hand = [card for card in hand if Rules.is_trump(card)]
                if trumps_on_hand:
                    valid_moves = trumps_on_hand
                else:
                    valid_moves = hand
            else:
                # farbe angespielt
                # led card is not a trump, so a card of the leading suit must be played if available
                leading_suits_cards = [card for card in hand if card.suit == led_card.suit]
                if leading_suits_cards:
                    valid_moves = leading_suits_cards
                else:
                    valid_moves = hand
        if not valid_moves:
            # there cant be no valid moves, an error has to have occurred
            raise ValueError("No valid moves found, which should not happen in a valid game.")
        return valid_moves

    @staticmethod
    def get_points(card: Card):
        return Rules.points_per_card[card.rank]
