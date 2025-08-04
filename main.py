from player import Player
from rules import Rules, Stich

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
    stich.add_card(player2.hand[0], player2)
    stich.add_card(player3.hand[0], player3)
    stich.add_card(player4.hand[0], player4)

    print("\nStich:")
    for card, player in stich.played_cards.items():
        print(f"\t{card} von {player}")

    winning_player, winning_card = rules.determine_winner_on_stich(stich)
    print(f"Gewinner: {winning_player} mit {winning_card}")