"""
The program of Joker Game (In Pairs). Run the following code to play Joker.

This file includes the following functions:
                1. play_game_in_pairs() => playing 4 sets, 16 hands (16 * 9 tricks)

"""

from Game_In_Pairs.Basic_Functions.get_players_and_cards import get_players_order
from Game_In_Pairs.Play_First_Set.play_first_set import play_first_set
from Game_In_Pairs.Play_Second_Set.play_second_set import play_second_set
from Game_In_Pairs.Play_Third_Set.play_third_set import play_third_set
from Game_In_Pairs.Play_Fourth_Set.play_fourth_set import play_fourth_set
from Game_In_Pairs.Basic_Functions.get_players_scores_functions import create_game_scores_table


def play_game_in_pairs():
    original_players_order = get_players_order(hand_number=0)
    perfect_match_scores = {f"{player}": [] for player in original_players_order}

    first_set_scores, perfect_match_scores = play_first_set(original_players_order,
                                                            perfect_match_scores={f"{player}": [] for player in
                                                                                  original_players_order})
    # print(f"N1: {perfect_match_scores}")
    second_set_scores, perfect_match_scores = play_second_set(original_players_order,
                                                              perfect_match_scores={f"{player}": [] for player in
                                                                                    original_players_order})
    # print(f"N2: {perfect_match_scores}")
    third_set_scores, perfect_match_scores = play_third_set(original_players_order,
                                                            perfect_match_scores={f"{player}": [] for player in
                                                                                  original_players_order})
    # print(f"N3: {perfect_match_scores}")
    fourth_set_scores, perfect_match_scores = play_fourth_set(original_players_order,
                                                              perfect_match_scores={f"{player}": [] for player in
                                                                                    original_players_order})
    # print(f"N4: {perfect_match_scores}")
    winner_team, winner_score, game_scores_table = create_game_scores_table(first_set_scores, second_set_scores,
                                                                            third_set_scores, fourth_set_scores)

    return winner_team, winner_score, game_scores_table


def main():
    pass


if __name__ == '__main__':
    main()
