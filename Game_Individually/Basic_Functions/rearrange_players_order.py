# The program of Joker Game

# This file includes the following functions:
#                    1. rearrange_players_order_for_next_trick()
#


def rearrange_players_order_for_next_trick(trick_winner_player, players_order, players_and_cards):
    rearranged_players_and_cards = {}
    temp_list_1 = []
    temp_list_2 = []
    for c in players_order:
        if c == trick_winner_player:
            index = players_order.index(c)
            temp_list_1.append(players_order[index:])
            temp_list_2.append(players_order[:index])

    combine_lists = temp_list_1 + temp_list_2
    players_order = [player for sublist in combine_lists for player in sublist]

    for player in players_order:
        if player in players_and_cards:
            rearranged_players_and_cards[player] = players_and_cards[player]

    return rearranged_players_and_cards


def main():
    pass


if __name__ == '__main__':
    main()
