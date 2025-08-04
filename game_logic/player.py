from game_logic.card import Card
from game_logic.rules import Rules


class Player:
    def __init__(self, name):
        self.name: str = name
        self.hand: list = list()

    def receive_cards(self, cards: list[Card]) -> None:
        self.hand: list = cards

    def play_card(self, first_card_played: Card) -> Card:
        # todo: implement agent logic
        valid_moves: list[Card] = Rules.get_valid_moves(self.hand, first_card_played)
        return valid_moves[0]

    def __repr__(self):
        return f"Spieler {self.name}"
