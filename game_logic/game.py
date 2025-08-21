from game_logic.basicplayer import BasicPlayer
from game_logic.rules import Multiplier, Rules
from game_logic.team import Team
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game_logic.round import Round


class Game:
    def __init__(self, players_ordered: list[BasicPlayer]):
        self.players: list[BasicPlayer] = players_ordered
        self.teams: list[Team] = [Team([players_ordered[0], players_ordered[2]]),
                                  Team([players_ordered[1], players_ordered[3]])]
        self.points: dict[Team, int] = {team: 0 for team in self.teams}
        self.player_to_play_first: BasicPlayer = players_ordered[0]

    def play_game(self) -> "Team":
        from game_logic.round import Round
        while not self.is_game_over():
            round: Round = Round(self, self.player_to_play_first)
            winning_team, points, multiplier = round.play_round()
            self.update_points(winning_team, points, multiplier)
            self.update_who_is_in_turn()
        return self.determine_winning_team_on_game_over()

    def is_game_over(self) -> bool:
        return any(self.points[team] >= 21 for team in self.teams)

    def determine_winning_team_on_game_over(self) -> Team | None:
        if self.points[self.teams[0]] >= 21:
            return self.teams[0]
        else:
            return self.teams[1]

    def update_points(self, team: Team, round_points: int, multiplier: Multiplier) -> None:
        if team is not None:
            game_points = Rules.get_game_points(round_points, multiplier)
            self.points[team] += game_points

    def update_who_is_in_turn(self) -> None:
        current_index: int = self.players.index(self.player_to_play_first)
        next_index: int = (current_index + 1) % len(self.players)
        self.player_to_play_first: BasicPlayer = self.players[next_index]
