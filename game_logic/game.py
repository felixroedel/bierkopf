from game_logic.player import Player
from game_logic.round import Round
from game_logic.team import Team


class Game:
    def __init__(self, players_ordered: list[Player]):
        self.players: list[Player] = players_ordered
        self.teams: list[Team] = [Team([players_ordered[0], players_ordered[2]]), Team([players_ordered[1], players_ordered[3]])]
        self.points: dict[Team, int] = {team: 0 for team in self.teams}
        self.player_to_play_first: Player = players_ordered[0]

    def play_game(self) -> Team:
        while not self.is_game_over():
            round: Round = Round(self, self.player_to_play_first)
            round.play_round()
            self.update_points()
            self.update_who_is_in_turn()
        return self.determine_winning_team_on_game_over()

    def is_game_over(self) -> bool:
        return any(self.points[team] >= 21 for team in self.teams)

    def determine_winning_team_on_game_over(self):
        if self.points[self.teams[0]] >= 21:
            return self.teams[0]
        elif self.points[self.teams[1]] >= 21:
            return self.teams[1]
        return None

    def update_points(self):
        pass

    def update_who_is_in_turn(self) -> None:
        current_index: int = self.players.index(self.player_to_play_first)
        next_index: int = (current_index + 1) % len(self.players)
        self.player_to_play_first: Player = self.players[next_index]