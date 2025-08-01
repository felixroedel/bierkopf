from player import Player
from rules import Rules

if __name__ == '__main__':
    rules = Rules()
    player1 = Player("1")
    player2 = Player("2")
    player3 = Player("3")
    player4 = Player("4")

    players = [player1, player2, player3, player4]
    hands = rules.deal_cards()
    for i, player in enumerate(players):
        player.receive_cards(hands[i])

    for player in players:
        print(f"{player} hat:")
        for card in player.hand:
            print(f"\t{card}")
