# The program of playing first set (4 hands (4 * 9 tricks)

from play_one_hand import play_one_hand
from Game_Individually.Basic_Functions.players_calls_functions import player_calls

players_and_first_set_scores = {}


def play_four_hands():
    global players_and_first_set_scores

    players_order, players_and_cards, players_calls, total_round_score, chosen_trump = player_calls()

    for i in range(4):
        play_one_hand()


def main():
    # play_four_hands()
    # print(players_and_first_set_scores)
    pass


if __name__ == '__main__':
    main()
