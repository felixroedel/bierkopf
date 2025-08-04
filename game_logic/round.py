from game_logic.game import Game
from game_logic.player import Player
from game_logic.rules import Rules


class Round:
    def __init__(self, game: Game, player_to_play_first: Player):
        self.game: Game = game
        self.remaining_cards_in_deck = Rules.get_all_cards()
        self.player_in_turn: Player = player_to_play_first

    def start_round(self):
        hands = Rules.deal_cards()
        for i, player in enumerate(self.game.players):
            player.receive_cards(hands[i])
            Rules.logger.info(f"Cards have been dealt to player {player.name}: {player.hand}")

    def play_round(self):
        self.start_round()
        while not self.is_round_over():
            # todo
            pass

    def is_round_over(self) -> bool:
        return len(self.remaining_cards_in_deck) == 0
