# The program of Joker Game

# This file includes the following functions:
#                    1. joker_is_first()
#                    2. joker_is_not_first()
#

from Game_Individually.Basic_Functions.get_players_and_cards import SUITS


def joker_is_first(player_choice_card, joker_choice, joker_case):
    player_action = input("Choose: Want Highest ('WANT') or Don't Want ('TAKE')? ")
    while player_action != "WANT" and player_action != "TAKE":
        player_action = input("Wrong input. Choose: Want Highest ('WANT') or Don't Want ('TAKE')? ")
    joker_choice = player_action

    if player_action == "WANT":
        want_suit = input("Which suit of cards do you want with highest ranks? ")
        while want_suit not in SUITS:
            want_suit = input("Enter valid suit. Which suit of cards do you want with highest ranks? ")
        joker_case.append(player_choice_card)

    if player_action == "TAKE":
        take_suit = input("Which suit of card do you want to take? ")
        while take_suit not in SUITS:
            take_suit = input("Enter valid suit. Which suit of card do you want to take? ")


def joker_is_not_first(player_choice_card, joker_case):
    player_joker_choice = input("Do you want to take cards by Joker or not? (YES/NO) ").upper()
    while player_joker_choice != "YES" and player_joker_choice != "NO":
        player_joker_choice = input("Enter YES or NO. "
                                    "Do you want to take cards by Joker or not? (YES/NO) ").upper()
    if player_joker_choice == "YES":
        joker_case.append(player_choice_card)


def main():
    pass


if __name__ == '__main__':
    main()