# The program of playing first set (4 hands (4 * 9 tricks)

from play_one_hand import play_one_hand
from Game_Individually.Basic_Functions.calculate_scores_functions import create_set_scores_table
from Game_Individually.Basic_Functions.calculate_scores_functions import perfect_match


def play_four_hands():
    hand_number = 0
    temp_players_order = None
    first_set_scores = []
    for _ in range(4):
        temp_players_order = play_one_hand(first_set_scores, hand_number, temp_players_order)
        print(temp_players_order)
        hand_number += 1

    players_and_first_set_scores = create_set_scores_table(first_set_scores)
    print(players_and_first_set_scores)


def main():
    play_four_hands()
    print(perfect_match)

    # pass


if __name__ == '__main__':
    main()
