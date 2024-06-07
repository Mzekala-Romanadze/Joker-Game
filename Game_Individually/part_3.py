# The program of Joker Game

# This file includes the following functions:
#                    1. players_calls()
#                    2. print_players_calls()
#

from part_1 import TOTAL_ROUND_CALL
from part_2 import deal_cards


def player_calls():
    players_and_cards, chosen_trump, players_order = deal_cards()

    players_calls = {}

    card_dealer = players_order[-1]
    total_round_score = 0

    for player, cards in players_and_cards.items():
        print(f"{player}'s cards: {cards} ")
        if player == card_dealer:
            unavailable_score = TOTAL_ROUND_CALL - total_round_score
            players_calls[player] = int(input(f"{player} what's your call? (if pass enter '0') "))
            while players_calls[player] == unavailable_score:
                players_calls[player] = int(input(f"{player}, {unavailable_score} is unavailable. choose another "
                                                  f"call: "))
            total_round_score += players_calls[player]
            break
        players_calls[player] = int(input(f"{player} what's your call? (if pass enter '0') "))
        total_round_score += players_calls[player]

    return players_order, players_and_cards, players_calls, total_round_score, chosen_trump


def print_players_calls():
    _, _, players_calls, total_round_score, _ = player_calls()
    print(players_calls)
    print(f"The Players' calls in total: {total_round_score}")


def main():
    pass
    # print_players_calls()


if __name__ == '__main__':
    main()
