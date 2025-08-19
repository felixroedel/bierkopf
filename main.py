from game_logic.player import Player
from game_logic.rules import Rules
from game_logic.stich import Stich

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

    stich = Stich(player1.hand[0], player1)
    print(f"\nErster Spieler: {player1} spielt {stich.first_card_played}")
    for player in players[1:]:
        valid = Rules.get_valid_moves(player.hand, stich.first_card_played)
        print(f"{player} kann spielen: {valid}")
        stich.add_card(player.play_card(valid[0]), player)

    print("\nStich:")
    for card, player in stich.played_cards.items():
        print(f"\t{card} von {player}")

    winning_player, winning_card, points = rules.determine_winner_on_stich(stich)
    print(f"Gewinner: {winning_player} mit {winning_card} und {points} Punkten.")