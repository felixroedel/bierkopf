from game_logic.basicplayer import BasicPlayer


class Team:
    def __init__(self, players: list[BasicPlayer]):
        self.players: list[BasicPlayer] = players

    def __repr__(self):
        return f"Team({', '.join(player.__repr__() for player in self.players)})"
