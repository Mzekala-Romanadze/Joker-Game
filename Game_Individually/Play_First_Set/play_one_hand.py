# The program of playing 1 hand (9 tricks, 36 cards)

from Game_Individually.Play_First_Set.play_one_trick import play_one_trick
from Game_Individually.Basic_Functions.rearrange_players_order import rearrange_players_order_for_next_trick

players_and_one_hand_scores = {}


def play_one_hand(players_order, players_and_cards, chosen_trump):
    global players_and_one_hand_scores

    players_and_one_hand_scores = {f"{player}": 0 for player in players_order}
    trick_winner_player = None

    for _ in range(9):
        play_one_trick(players_and_cards, chosen_trump, trick_winner_player)
        players_and_cards, players_order = rearrange_players_order_for_next_trick(trick_winner_player, players_order,
                                                                                  players_and_cards)
        print(players_and_one_hand_scores)


def main():
    # print(players_and_one_hand_scores)
    pass


if __name__ == '__main__':
    main()
