from game_logic.basicplayer import BasicPlayer
from game_logic.card import Card


class DumbPlayer(BasicPlayer):
    def choose_card(self, valid_moves: list[Card]) -> Card:
        """Selects the first valid card from the list of valid moves."""
        return valid_moves[0]
