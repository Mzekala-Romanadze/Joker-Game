"""
The program of Joker Game (Individually). Run the following code to play Joker.

This file includes the following functions:
                1. play_game() => playing 4 sets, 16 hands (16 * 9 tricks)

"""

from Game_Individually.Play_First_Set.play_first_set import play_first_set
from Game_Individually.Play_Second_Set.play_second_set import play_second_set
from Game_Individually.Play_Third_Set.play_third_set import play_third_set
from Game_Individually.Play_Fourth_Set.play_fourth_set import play_fourth_set
from Game_Individually.Basic_Functions.get_players_scores_functions import create_game_scores_table


def play_game_individually():
    first_set_scores = play_first_set()
    second_set_scores = play_second_set()
    third_set_scores = play_third_set()
    fourth_set_scores = play_fourth_set()

    winner_player, winner_score, game_scores_table = create_game_scores_table(first_set_scores, second_set_scores, third_set_scores, fourth_set_scores)

    return winner_player, winner_score, game_scores_table


def main():
    print("Hello Players, you play Individually ")
    print("Be mindful of every decision. Success is in the details.")
    winner_player, winner_score, game_scores_table = play_game_individually()

    if len(winner_player) > 1:
        print(f"Game is over! There are more than one winner: {winner_player} Congratulations! "
              f"You won the game by {winner_score} points. ")
    else:
        print(f"Game is over! {winner_player} Congratulations! You won the game by {winner_score} points. ")

    print(f"The players and scores: {game_scores_table}")


if __name__ == '__main__':
    main()
