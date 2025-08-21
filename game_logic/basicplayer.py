from abc import abstractmethod, ABC

from game_logic.card import Card


class BasicPlayer(ABC):
    def __init__(self, name):
        self.name: str = name
        self.hand: list = list()

    def receive_cards(self, cards: list[Card]) -> None:
        self.hand: list = cards

    def play_card(self, first_card_played: Card | None) -> Card:
        from game_logic.rules import Rules
        valid_moves: list[Card] = Rules.get_valid_moves(self.hand, first_card_played)
        card_to_play: Card = self.choose_card(valid_moves)
        self.hand.remove(card_to_play)
        return card_to_play

    @abstractmethod
    def choose_card(self, valid_moves: list[Card]) -> Card:
        pass

    def __repr__(self):
        return f"{self.__class__.__name__} {self.name}"
