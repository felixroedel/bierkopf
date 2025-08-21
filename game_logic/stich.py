from game_logic.card import Card, Suit
from game_logic.basicplayer import BasicPlayer


class Stich:
    def __init__(self, first_played_card: Card, player: BasicPlayer):
        self.first_card_played: Card = first_played_card
        self.leading_suit: Suit = first_played_card.suit
        self.played_cards: dict[Card, BasicPlayer] = {first_played_card: player}

    def add_card(self, card: Card, player: BasicPlayer):
        self.played_cards[card] = player
