from game_logic.basicplayer import BasicPlayer
from game_logic.rules import Rules, Multiplier
from typing import TYPE_CHECKING

from game_logic.stich import Stich

if TYPE_CHECKING:
    from game_logic.game import Game
    from game_logic.team import Team


class Round:
    def __init__(self, game: "Game", player_to_play_first: BasicPlayer):
        self.game: "Game" = game
        self.remaining_cards_in_deck = Rules.get_all_cards()
        self.player_in_turn: BasicPlayer = player_to_play_first
        self.points: dict["Team", int] = {team: 0 for team in self.game.teams}
        self.multiplier: dict["Team", Multiplier] = {team: Multiplier.NORMAL for team in self.game.teams}
        self.stichs: list[Stich] = list()

    def start_round(self):
        hands = Rules.deal_cards()
        for i, player in enumerate(self.game.players):
            player.receive_cards(hands[i])
            Rules.logger.info(f"Cards have been dealt to player {player.name}: {player.hand}")

    def play_round(self):
        self.start_round()
        while not self.is_round_over():
            stich = Stich(self.player_in_turn.play_card(first_card_played=None), self.player_in_turn)
            Rules.logger.info(f"First card played by {self.player_in_turn.name}: {stich.first_card_played}")
            for player in self.game.players:
                if player != self.player_in_turn:
                    played_card = player.play_card(stich.first_card_played)
                    stich.add_card(played_card, player)
                    Rules.logger.info(f"{player.name} plays {played_card}")
            player, winning_card, points = Rules.determine_winner_on_stich(stich)
            Rules.logger.info(f"Winner of the stich: {player.name} with {winning_card} and {points} points.")
            self.update_points(player, points)
            self.stichs.append(stich)
            self.remaining_cards_in_deck = [card for card in self.remaining_cards_in_deck if
                                            card not in stich.played_cards]
        return self.determine_winning_team_on_round_over()

    def update_points(self, player: BasicPlayer, points: int) -> None:
        team = self.game.teams[0] if player in self.game.teams[0].players else self.game.teams[1]
        self.points[team] += points
        Rules.logger.info(f"Updated points for {player.name} in {team}: {self.points[team]}")

    def is_round_over(self) -> bool:
        return len(self.remaining_cards_in_deck) == 0

    def determine_winning_team_on_round_over(self) -> ("Team", int, Multiplier):
        if self.points[self.game.teams[0]] == self.points[self.game.teams[1]]:
            if max(self.multiplier.values()) != Multiplier.NORMAL:
                losing_team = self.game.teams[0] if self.multiplier[self.game.teams[0]] == Multiplier.SPRITZ else \
                    self.game.teams[1]
                winning_team = self.game.teams[0] if self.multiplier[self.game.teams[0]] != Multiplier.SPRITZ else \
                    self.game.teams[1]
                Rules.logger.info(
                    f"Round over with a tie, but team {losing_team} did SPRITZ. Winning team: {winning_team}.")
                return winning_team, 60, self.multiplier[winning_team]
            else:
                Rules.logger.info("Round over with a tie and no SPRITZ. No team wins.")
                return None, 0, Multiplier.NORMAL
        else:
            winning_team = max(self.points, key=self.points.get)
            multiplier = max(self.multiplier.values())
            points = self.points[winning_team]
            Rules.logger.info(
                f"Round over. Winning team: {winning_team} with {points} points and multiplier: {multiplier}.")
            return winning_team, points, multiplier
