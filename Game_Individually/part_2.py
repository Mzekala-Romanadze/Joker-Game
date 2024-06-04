# The program of Joker Game

# This file includes the following functions:
#                    1. get_players_order()
#                    2. deal_cards()
#                    3. print_cards()


import random

from part_1 import create_and_shuffle_cards, get_player_names


def get_players_order(players):
    first_card_dealer = random.choice(players)
    temp_list_1 = []
    temp_list_2 = []
    for player in players:
        if player == first_card_dealer:
            index = players.index(player)
            temp_list_1.append(players[index + 1:])
            temp_list_2.append(players[:index + 1])
    combine_lists = temp_list_1 + temp_list_2
    player_order = [player for sublist in combine_lists for player in sublist]
    return player_order


def deal_cards(players_order):
    deck = create_and_shuffle_cards()
    players_and_cards = {f'{player}': [] for player in players_order}

    for i in range(9):
        for player in players_and_cards:
            players_and_cards[player].append(deck.pop(0))

    return players_and_cards


def print_cards(players_and_cards):
    for player, cards in players_and_cards.items():
        print(f"{player}: {cards}")


def main():
    players = get_player_names()
    players_order = get_players_order(players)
    players_and_cards = deal_cards(players_order)
    print_cards(players_and_cards)

    # print(players_order)
    # print(players_and_cards)


if __name__ == '__main__':
    main()
