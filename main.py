"""
The program of Joker Game. Run the following code to play Joker.

This file includes the following function:
            1. choose_game_type() => Individually or In pairs
            2. play_game() => playing 4 sets, 16 hands (16 * 9 tricks)

Firstly, the user should choose game type: Individually or In pairs

"""

from Game_In_Pairs.play_in_pairs import play_game_in_pairs
from Game_Individually.play_individually import play_game_individually


def choose_game_type():
    user_choice = input("Play Individually (I) or In Pairs (P)? ").upper()
    while user_choice != "I" and user_choice != "P":
        user_choice = input("Enter valid Symbol: Individually (I) or In Pairs (P) ").upper()
    if user_choice == "I":
        return "Individually"
    if user_choice == "P":
        return "In Pairs"


def play_game():
    game_type = choose_game_type()

    if game_type == "Individually":
        print("Hello Players, you play Individually ")
        print("Be mindful of every decision. Success is in the details.")
        play_game_individually()

    if game_type == "In Pairs":
        print("Hello Players, you play In Pairs ")
        print("Be mindful of every decision. Success is in the details and teamwork.")
        play_game_in_pairs()


def main():
    # play_game()
    pass


if __name__ == '__main__':
    main()
