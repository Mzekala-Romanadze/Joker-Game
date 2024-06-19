"""
The program of Joker Game. This file includes the following functions:
            1. play_first_set() => playing 4 hands (4 * 9 tricks)

"""

from play_one_hand import play_one_hand
from Game_Individually.Basic_Functions.get_players_scores_functions import (create_set_scores_table,
                                                                            find_perfect_match_player,
                                                                            create_final_set_scores)
from Game_Individually.Basic_Functions.get_players_scores_functions import perfect_match_scores


def play_first_set():
    hand_number = 0
    temp_players_order = None
    first_set_scores = []
    for _ in range(4):
        temp_players_order, first_set_scores = play_one_hand(first_set_scores, hand_number, temp_players_order)
        print(temp_players_order)
        hand_number += 1

    players_and_first_set_scores = create_set_scores_table(first_set_scores)
    print(players_and_first_set_scores)

    perfect_match = find_perfect_match_player(perfect_match_scores)

    if perfect_match is None:
        print(players_and_first_set_scores)
        return players_and_first_set_scores
    else:
        print(perfect_match)
        final_version = create_final_set_scores(players_and_first_set_scores, perfect_match)
        print(final_version)
        return final_version


def main():
    pass


if __name__ == '__main__':
    main()
