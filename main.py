from ai.dumb_player import DumbPlayer
from game_logic.game import Game
from game_logic.rules import Rules

if __name__ == '__main__':
    player1 = DumbPlayer("1")
    player2 = DumbPlayer("2")
    player3 = DumbPlayer("3")
    player4 = DumbPlayer("4")

    players = [player1, player2, player3, player4]

    game = Game(players)
    winning_team = game.play_game()

    Rules.logger.info(f"Winning team: {winning_team}")
