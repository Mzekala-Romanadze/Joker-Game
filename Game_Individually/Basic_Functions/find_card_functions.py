# The program of Joker Game

# This file includes the following functions:
#                    1. find_highest_suit_card()
#                    2. find_highest_value_card()
#                    3. find_winner_card_of_trick()
#

from Game_Individually.Basic_Functions.get_players_and_cards import RANK_VALUES


def find_highest_suit_card(cards, wanted_suit):
    player_suit_cards = [card for card in cards if wanted_suit in card]

    highest_card = None
    highest_rank_value = -1

    for card in player_suit_cards:
        rank = card.split(' of ')[0]
        rank_value = RANK_VALUES[rank]
        if rank_value > highest_rank_value:
            highest_rank_value = rank_value
            highest_card = card

    # print("The highest card is:", highest_card)
    return highest_card


def find_highest_value_card(table_cards, chosen_trump, joker_case):
    highest_card = None
    highest_rank_value = -1

    for card in table_cards:
        rank, suit = card.split(' of ')

        if rank == "Joker":
            continue

        if suit == chosen_trump:
            rank_value = RANK_VALUES[rank] + 100
        else:
            rank_value = RANK_VALUES[rank]

        if rank_value > highest_rank_value:
            highest_rank_value = rank_value
            highest_card = card

    # print("The highest card is:", highest_card)
    # index = table_cards.index(highest_card)
    return highest_card


def find_winner_card_of_trick(joker_case, trump_joker_case, chosen_trump, table_cards):
    winner_card = None

    if len(joker_case) == 1 and len(trump_joker_case) == 1:
        winner_card = trump_joker_case[0]
    elif len(joker_case) == 1 and len(trump_joker_case) > 1:
        winner_card = find_highest_suit_card(trump_joker_case, chosen_trump)
    elif len(joker_case) == 1:
        winner_card = joker_case[0]
    elif len(joker_case) == 2:
        winner_card = joker_case[1]
    else:
        winner_card = find_highest_value_card(table_cards, chosen_trump, joker_case)

    return winner_card


def main():
    pass


if __name__ == '__main__':
    main()
