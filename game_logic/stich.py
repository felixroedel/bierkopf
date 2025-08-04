from game_logic.card import Card, Suit
from game_logic.player import Player


class Stich:
    def __init__(self, first_played_card: Card, player: Player):
        self.first_card_played: Card = first_played_card
        self.leading_suit: Suit = first_played_card.suit
        self.played_cards: dict[Card, Player] = {first_played_card: player}

    def add_card(self, card: Card, player: Player):
        self.played_cards[card] = player
