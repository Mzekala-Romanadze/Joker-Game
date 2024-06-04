# The program of Joker Game (Individually)

# This file includes the following functions:
#                    1.

from part_1 import get_player_names, create_and_shuffle_cards, choose_game_type


def main():
    players = get_player_names()
    deck_of_cards = create_and_shuffle_cards()
    game_type = choose_game_type()

    print(players)
    print(deck_of_cards)
    print(game_type)

    if game_type == "Individually":
        print("Start this Game")


if __name__ == '__main__':
    main()
