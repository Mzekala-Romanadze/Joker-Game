# The program of Joker Game

# This file includes the following functions:
#                    1. check_card()
#


def check_card(player_choice_card, cards):
    while player_choice_card not in cards:
        player_choice_card = input("You do not have this card. Choose another which you want to be led: ")


def main():
    pass


if __name__ == '__main__':
    main()
