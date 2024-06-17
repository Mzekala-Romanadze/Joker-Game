# The program of Joker Game

# This file includes the following functions:
#                    1. get_card_dealer()
#                    2. deal_cards()
#                    3. choose_trump()
#                    4. print_cards()
#

from Game_Individually.Basic_Functions.get_players_and_cards import get_players_order, create_and_shuffle_cards
from Game_Individually.Basic_Functions.rearrange_players_order import rearrange_players_order_for_next_hand

# def get_card_dealer():
#     players_order = get_players_order()
#     card_dealer = players_order[3]
#     return players_order, card_dealer


def deal_cards(players_order):
    deck = create_and_shuffle_cards()

    print(f"Player order: {players_order}: ")

    players_and_cards = {f"{player}": [] for player in players_order}
    first_player = players_order[0]
    three_cards_to_show = players_and_cards[first_player]
    chosen_trump = None

    for i in range(9):
        for player in players_and_cards:
            players_and_cards[player].append(deck.pop(0))
        if i == 2:
            print(f"{first_player}: {three_cards_to_show}")
            chosen_trump = choose_trump(first_player)

    return players_and_cards, chosen_trump, players_order


def choose_trump(first_player):
    # chosen_trump = input(f"{first_player} Please choose trump: Heart ('H'), Diamond ('D'), Spade ('S'), "
    #                      f"Club ('C') or Nothing ('N') ").upper()
    # while chosen_trump not in TRUMP:
    #     chosen_trump = input(f"{first_player} Please choose valid trump: Heart ('H'), Diamond ('D'), Spade ('S'), "
    #                          f"Club ('C') or Nothing ('N') ").upper()
    # # return chosen_trump
    return "Club"


def print_cards(players_and_cards, chosen_trump):
    print(f"The trump of the round is {chosen_trump}")
    for player, cards in players_and_cards.items():
        print(f"{player}'s cards: {cards}")


def main():
    pass
    # players_and_cards, chosen_trump = deal_cards()
    # print_cards(players_and_cards, chosen_trump)

    # print(players_and_cards)
    # print(chosen_trump)


if __name__ == '__main__':
    main()
