from card import Card


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def receive_cards(self, cards: list[Card]) -> None:
        self.hand = cards

    def play_card(self):
        # this is the crucial part
        pass

    def __repr__(self):
        return f"Spieler {self.name}"
